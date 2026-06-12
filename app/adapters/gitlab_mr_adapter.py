from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class GitLabConfigError(RuntimeError):
    """Raised when GitLab API mode is missing required configuration."""


class LocalMRCommentAdapter:
    """Writes the MR briefing to a local markdown file."""

    def __init__(self, output_path: str | Path) -> None:
        self.output_path = Path(output_path)

    def post_comment(self, body: str) -> Path:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(body.rstrip() + "\n", encoding="utf-8")
        return self.output_path


@dataclass(frozen=True)
class GitLabPostResult:
    posted: bool
    dry_run: bool
    endpoint: str
    project_id: str
    merge_request_iid: str
    note_id: int | None = None
    web_url: str | None = None
    response: dict[str, Any] | None = None

    def as_log(self) -> dict[str, Any]:
        return {
            "posted": self.posted,
            "dry_run": self.dry_run,
            "endpoint": self.endpoint,
            "project_id": self.project_id,
            "merge_request_iid": self.merge_request_iid,
            "note_id": self.note_id,
            "web_url": self.web_url,
        }


class GitLabMRCommentAdapter:
    """Posts an MR briefing as a GitLab merge request note.

    This adapter intentionally uses the GitLab Notes API, not a line-level diff
    discussion. The first working integration target is a reviewer-ready MR
    overview comment. Line-level comments can be added later through the
    Discussions API if needed.
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: str | None,
        project_id: str,
        merge_request_iid: str,
        dry_run: bool = False,
        timeout_seconds: float = 20.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.project_id = str(project_id)
        self.merge_request_iid = str(merge_request_iid)
        self.dry_run = dry_run
        self.timeout_seconds = timeout_seconds

        if not self.project_id:
            raise GitLabConfigError("Missing GitLab project id/path.")
        if not self.merge_request_iid:
            raise GitLabConfigError("Missing GitLab merge request IID.")
        if not self.dry_run and not self.token:
            raise GitLabConfigError(
                "Missing GITLAB_TOKEN. Set it in the environment or run with --dry-run."
            )

    @classmethod
    def from_env(
        cls,
        *,
        project_id: str | None = None,
        merge_request_iid: str | None = None,
        base_url: str | None = None,
        dry_run: bool = False,
    ) -> "GitLabMRCommentAdapter":
        return cls(
            base_url=base_url or os.getenv("GITLAB_BASE_URL", "https://gitlab.com"),
            token=os.getenv("GITLAB_TOKEN"),
            project_id=project_id or os.getenv("GITLAB_PROJECT_ID", ""),
            merge_request_iid=merge_request_iid or os.getenv("GITLAB_MR_IID", ""),
            dry_run=dry_run,
        )

    def endpoint(self) -> str:
        encoded_project = urllib.parse.quote(self.project_id, safe="")
        encoded_mr = urllib.parse.quote(self.merge_request_iid, safe="")
        return (
            f"{self.base_url}/api/v4/projects/{encoded_project}"
            f"/merge_requests/{encoded_mr}/notes"
        )

    def post_comment(self, body: str) -> GitLabPostResult:
        endpoint = self.endpoint()
        if self.dry_run:
            return GitLabPostResult(
                posted=False,
                dry_run=True,
                endpoint=endpoint,
                project_id=self.project_id,
                merge_request_iid=self.merge_request_iid,
            )

        payload = urllib.parse.urlencode({"body": body.rstrip()}).encode("utf-8")
        request = urllib.request.Request(
            endpoint,
            data=payload,
            method="POST",
            headers={
                "PRIVATE-TOKEN": self.token or "",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Accept": "application/json",
                "User-Agent": "orbit-guardrail-agent/0.1",
            },
        )

        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"GitLab API returned HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"GitLab API request failed: {exc}") from exc

        parsed = json.loads(raw) if raw else {}
        return GitLabPostResult(
            posted=True,
            dry_run=False,
            endpoint=endpoint,
            project_id=self.project_id,
            merge_request_iid=self.merge_request_iid,
            note_id=parsed.get("id"),
            web_url=parsed.get("web_url"),
            response=parsed,
        )

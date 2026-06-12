from __future__ import annotations

from pathlib import Path


class LocalMRCommentAdapter:
    """Writes the MR briefing to a local markdown file.

    Later this can be replaced by a GitLab API adapter that posts the same body
    to a Merge Request discussion.
    """

    def __init__(self, output_path: str | Path) -> None:
        self.output_path = Path(output_path)

    def post_comment(self, body: str) -> Path:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(body.rstrip() + "\n", encoding="utf-8")
        return self.output_path

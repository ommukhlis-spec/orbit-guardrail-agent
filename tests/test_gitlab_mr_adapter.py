from app.adapters.gitlab_mr_adapter import GitLabMRCommentAdapter


def test_gitlab_adapter_dry_run_encodes_project_path() -> None:
    adapter = GitLabMRCommentAdapter(
        base_url="https://gitlab.com/",
        token=None,
        project_id="group/demo project",
        merge_request_iid="12",
        dry_run=True,
    )

    result = adapter.post_comment("hello")

    assert result.posted is False
    assert result.dry_run is True
    assert result.project_id == "group/demo project"
    assert result.merge_request_iid == "12"
    assert "group%2Fdemo%20project" in result.endpoint
    assert result.endpoint.endswith("/merge_requests/12/notes")

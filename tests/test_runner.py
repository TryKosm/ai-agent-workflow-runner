from pathlib import Path

from workflow_runner.core import Task
from workflow_runner.runner import execute_plan


def test_execute_plan_writes_report(tmp_path: Path) -> None:
    calls = []

    def handler(name: str) -> None:
        calls.append(name)

    execute_plan([Task("fetch"), Task("rank")], handler, tmp_path / "out.json")
    assert calls == ["fetch", "rank"]


def test_run_task_retries_until_success(tmp_path: Path) -> None:
    attempts = {"count": 0}

    def flaky(_: str) -> None:
        attempts["count"] += 1
        if attempts["count"] < 2:
            raise RuntimeError("retry")

    execute_plan([Task("fetch", max_retries=1)], flaky, tmp_path / "retry.json")
    assert attempts["count"] == 2

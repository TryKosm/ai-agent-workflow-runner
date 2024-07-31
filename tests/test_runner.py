from pathlib import Path

from workflow_runner.core import Task
from workflow_runner.runner import execute_plan


def test_execute_plan_writes_report(tmp_path: Path) -> None:
    calls = []

    def handler(name: str) -> None:
        calls.append(name)

    execute_plan([Task("fetch"), Task("rank")], handler, tmp_path / "out.json")
    assert calls == ["fetch", "rank"]

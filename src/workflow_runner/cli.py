from __future__ import annotations

import argparse
from pathlib import Path

from .core import Task
from .runner import execute_plan


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="run_artifacts/report.json")
    args = parser.parse_args()
    tasks = [Task("retrieve"), Task("rank"), Task("answer")]
    execute_plan(tasks, lambda _: None, Path(args.output))

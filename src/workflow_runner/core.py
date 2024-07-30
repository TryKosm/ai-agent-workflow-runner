from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    name: str
    max_retries: int = 0


def run_task(task: Task, handler) -> int:
    attempts = 0
    while True:
        attempts += 1
        try:
            handler(task.name)
            return attempts
        except Exception:
            if attempts > task.max_retries:
                raise

#!/usr/bin/env python3
"""
Claude Code Hook: Python 파일 자동 lint/fix
- ruff check --fix: 린트 오류 자동 수정
- ruff format: 코드 포매팅
- ty check: 타입 체크 (오류 시 exit code 1로 Claude에게 수정 요청)
"""
import json
import os
import subprocess
import sys


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    file_path = input_data.get("tool_input", {}).get("file_path", "")

    # Python 파일만 처리
    if not file_path or not file_path.endswith(".py"):
        return 0

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if not project_dir:
        return 0

    os.chdir(project_dir)

    # 1. ruff check --fix
    subprocess.run(
        ["ruff", "check", "--fix", file_path],
        capture_output=True,
        text=True,
        timeout=30,
    )

    # 2. ruff format
    subprocess.run(
        ["ruff", "format", file_path],
        capture_output=True,
        text=True,
        timeout=30,
    )

    # 3. ty check (타입 오류 시 차단)
    result = subprocess.run(
        ["ty", "check", file_path],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        output = result.stdout.strip() or result.stderr.strip()
        if output:
            print(f"ty type error:\n{output}", file=sys.stderr)
        return 1  # 타입 오류 시 Hook 실패 → Claude가 수정하도록 함

    return 0


if __name__ == "__main__":
    sys.exit(main())

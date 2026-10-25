# Working on this student game

- Read SPEC.md and existing code before editing. Treat the agreed spec as current context; flag conflicts and unclear behavior before coding.
- The starter deliberately leaves RPS-001 unimplemented in game.py. Supplied shell tests do not prove the game rules.
- Keep RPS-001 to one independent round. No score, accounts, storage, new frontend framework, AI API, or OOP patterns unless separately agreed.
- Students use ChatGPT desktop for discussion, Codex in this folder for implementation, VS Code for inspection, and terminal Git over SSH. Do not substitute a Command Palette or Git GUI workflow.
- Run .venv/bin/python -m pytest. Add explicit expected outcomes from SPEC.md and a real request/result integration test with a fixed computer move. Do not derive expected answers from the implementation under test.
- Before asking the student to play, run checks, inspect the diff against the spec, fix identified problems, and report actual results and limitations. Never invent browser checks or claim a second AI review is independent proof.
- Preserve the student's agreed plan and issue link. Record concise actual checks and relative code/test links in SPEC.md. Keep detailed evidence in the PR; avoid temporary status such as 'not pushed'.
- No commits, pushes, or merges unless the student asks. Explain unexpected changed files. Keep .venv, caches, credentials, and local data out of Git.

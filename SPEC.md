# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

Agreed with the student: rock against paper loses; paper covers rock (explanation supplied with AI help). Implement all nine player-perspective outcomes with the supplied interface/server. Each choice starts an independent round. Test all nine literal outcomes, a real HTTP result, and a Chromium round/replay; fix only randomness. Reuse HTTP 400 missing/unsupported-input checks, including lizard. No scoring, storage, accounts, new framework, or AI API.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Implementation: [game.py](game.py), [unit and request tests](tests/test_game.py), [Chromium round/replay test](tests/e2e/test_round.py).
- Full local checks: student ran `.venv\Scripts\python.exe check.py` in PowerShell with Python 3.12.6 after the Windows fixture cleanup fix. Black: 11 files unchanged, PASS. Pylint: PASS. Non-browser pytest: 23 passed, 6 deselected (0.16s). Chromium: 6 passed, 23 deselected (14.99s). All configured checks passed. Earlier sandbox/cleanup failures were resolved or bypassed by running in the student's regular terminal.
- Review: compared game.py and both new test files against all nine expected outcomes and the agreed scope. Positive tests patch only computer randomness. Supplied server, interface, configuration, and negative assertions are unchanged.
- Test explanation: the literal rock/paper/lose case catches reversed winner rules or computer-perspective results. AI explained this example when the student was unsure; the student correctly predicted paper/rock/win afterward.
- Actual student browser observation: scissors against computer paper displayed a player win; scissors cuts paper. Student confirmed independent replay and Tab/Enter controls worked.
- Help: AI assisted with setup, implementation, tests, rule/test explanation, and this evidence record. The student supplied predictions and the actual browser observation.
- Issue: [RPS-001 #1](https://github.com/Khadija3005/is218-rps/issues/1).
- Pull request: [RPS-001 #2](https://github.com/Khadija3005/is218-rps/pull/2), closes #1.
- CI: [Final PR Python checks](https://github.com/Khadija3005/is218-rps/actions/runs/41490323250) passed on final PR commit `67e75f6` before merging.
- GitHub help: student created the issue and PR and pushed the branch because the connected integration denied writes.

- Windows fixture fix: the supplied development-server fixture now stops its own process tree on Windows before closing stdout, preventing a reloader child from hanging cleanup. Assertions and shared check settings remain intact. Reviewed this additional test-fixture change.

# Build a game you can trust—with AI

Turn this unfinished Rock, Paper, Scissors starter into a playable game. **Agree what correct means, guide AI, and check its work.** Practice a short spec, AI testing and review, and a GitHub change someone else can follow.

Use **ChatGPT desktop to discuss**, **Codex to edit and test**, **VS Code to inspect**, and your **class terminal for Git**. Keep the same project folder open in Codex and VS Code. No API key is needed.

**Try → Decide → Build → Check → Keep.** [Visual overview and help](https://kaw393939.github.io/218_spec/).

**Give AI a feedback loop.** The tools are prepared: **pytest** checks expected behavior, **Pylint** finds suspicious Python and standards violations, and **Black** checks consistent formatting. A small real-browser test checks the interface too. One command runs them locally and on GitHub. Passing means these checks found no problem—not that every requirement is proven.

Plan **positive** cases (valid wins, losses, and ties) and **negative** cases (missing or unsupported moves). Use quick **unit** tests for rules, **integration** tests for requests/results, and a few **end-to-end** browser checks for the player journey. [Short introduction and examples](https://kaw393939.github.io/218_spec/checks.html).

## 1. Try the starter

Use your class Python 3.12, VS Code, Git and GitHub SSH. Windows students use the class Ubuntu/WSL terminal; Mac students use Terminal. These commands work in both.

On [the starter](https://github.com/kaw393939/is218-rps-starter), choose **Use this template → Create a new repository**. Use your account, name it `my-rps`, choose **Public**, and leave **Include all branches** off. Leave the optional Copilot prompt blank. If the name is taken, choose another and use it below.

In your projects folder, replace `YOUR-USERNAME` with your GitHub username:

```sh
git clone git@github.com:YOUR-USERNAME/my-rps.git
cd my-rps
git remote -v
code .
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python check.py
.venv/bin/python run.py
```

The remote should name **your copy**, using `git@github.com:` for fetch and push. Chromium is a one-time test-browser download; checks use it automatically without opening a window. Look for **PASS** at each check stage, **even though the rules are unfinished**. The supplied tests check the shell, not RPS-001. Resolve a failed check using [Setup help](https://kaw393939.github.io/218_spec/setup.html) before proceeding.

Open **http://127.0.0.1:5050**. Expect three choices and **“Starter: game rules not built yet.”** Click a choice: no winner is expected yet. Leave this terminal running; code edits reload automatically.

Open a second terminal in this project folder for the remaining commands. Open this same folder as a local project in Codex. Stuck? [Setup help](https://kaw393939.github.io/218_spec/setup.html). Already have your copy running? Continue below; do not create another copy.

## 2. Decide what to build

Open `SPEC.md` in VS Code and attach it in ChatGPT desktop. Ask:

> Help me understand RPS-001. Do not code. Explain what the player should see. Propose a small test plan with positive/negative cases, explicit expected results, and unit/integration/E2E levels. Use the supplied checks where useful; avoid duplicate tests and extra features.

Read the nine-matchup table yourself. Whose perspective does “win” mean? Ask about anything unclear. Keep scoring for later. Save the agreed plan in **SPEC.md → Agreed plan**, replacing that section's starter text in VS Code. Carry the decisions, not the whole conversation.

In **your repository → Issues → New issue**, create **“RPS-001: Play a round”**. Use this short body, adjusting it to your agreed plan:

> Implement RPS-001 in SPEC.md. Show both choices and the correct result. A new choice starts another round. Check nine unit outcomes, a real submitted round, supplied invalid-input cases, and a short browser journey. No scoring yet.

Copy the issue URL into **SPEC.md → Work record**.

## 3. Build and let AI check first

In the second terminal:

```sh
git status --short --branch
git switch -c rps-001
```

Expect `## main...origin/main` and only your intended `SPEC.md` edit. If the branch already exists, use `git switch rps-001`.

In Codex, with **your cloned folder** open, ask:

> Read AGENTS.md, SPEC.md and the supplied test fixtures. Explain your implementation and test plan; flag conflicts before coding. After I approve, implement RPS-001 in game.py. Add tests/test_game.py with nine explicit unit outcomes and one real request/result integration check. Reuse the supplied negative request tests. Add tests/e2e/test_round.py for a real browser round and replay using live_server and page. Fix the computer choice, not the rule function. Run .venv/bin/python check.py and review the diff against the spec. Fix problems without weakening checks. Report actual results and remaining human checks. Do not commit or push.

Read its plan before approving. New tests should use the table's answers, not calculate expected answers with the winner function. Mark tests `unit`, `integration`, or `e2e`. The browser test uses a supplied temporary server; you do not need to manage another server or port for it.

## 4. Play, inspect, and give feedback

Refresh the local game, then choose a move to start a new round. Play several rounds: do both choices and the result make sense? Can you choose again? Try Tab and Enter too.

In the second terminal:

```sh
.venv/bin/python check.py
git diff
```

Press `q` if Git opens a scrolling view. Inspect `game.py` and its tests in VS Code. Ask AI to explain one positive case, one negative case, and why they use those test levels. Random clicking cannot reliably cover all nine matchups; deterministic tests do that.

During a fix, `.venv/bin/python check.py --fast` skips the browser for quicker feedback. Use the full command before review and the PR. For a formatting failure, `.venv/bin/python -m black *.py tests` applies the shared style; inspect the diff and rerun checks. Keep the tests and settings enabled.

Tell Codex what you actually saw. For a problem, describe what you did, expected, and saw; ask for a focused fix and retest. Ask it to replace the starter status in **SPEC.md → Work record** with actual checks and links to `game.py` and `tests/test_game.py`, preserving your plan and issue. Do not claim checks nobody performed.

## 5. Keep the reviewed change

Expect changes to `game.py`, `tests/test_game.py`, `tests/e2e/test_round.py`, and `SPEC.md`. Ask about any other changed files before keeping them.

```sh
git add game.py tests/test_game.py tests/e2e/test_round.py SPEC.md
git diff --cached
git commit -m "RPS-001: play a round"
git push -u origin rps-001
```

In **your repository → Pull requests → New pull request**, use base `main` and compare `rps-001`. Briefly describe the result and actual checks. Include **`Closes #N`** with your issue number. Inspect **Files changed**, wait for **Python checks** to pass, then merge when it matches the spec. Deploying a website is not part of this exercise.

**Done:** the game works locally, the PR is merged, its issue is closed, and the spec links to code and actual checks. Stop the server with Ctrl+C. You should be able to point to a rule, its code, and evidence that it works.

**Next time:** [RPS-002: first to two wins](NEXT.md). Keep that separate from your first PR.

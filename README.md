# Build a game you can trust—with AI

Turn this unfinished Rock, Paper, Scissors starter into a playable game. **Agree what correct means, guide AI, and check its work.** Practice a short spec, AI testing and review, and a GitHub change someone else can follow.

Use **ChatGPT desktop to discuss**, **Codex to edit and test**, **VS Code to inspect**, and your **class terminal for Git**. Keep the same project folder open in Codex and VS Code. No API key is needed.

**Try → Decide → Build → Check → Keep.** [Visual overview and help](https://kaw393939.github.io/218_spec/).

## 1. Try the starter

Use your class Python 3.12, VS Code, Git and GitHub SSH. Windows students use the class Ubuntu/WSL terminal; Mac students use Terminal. These commands work in both.

On [the starter](https://github.com/kaw393939/is218-rps-starter), choose **Use this template → Create a new repository**. Use your account, name it `my-rps`, choose **Public**, and leave **Include all branches** unchecked. If the name is taken, choose another and use it below.

In your projects folder, replace `YOUR-USERNAME` with your GitHub username:

```sh
git clone git@github.com:YOUR-USERNAME/my-rps.git
cd my-rps
git remote -v
code .
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python run.py
```

The remote should name **your copy**, using `git@github.com:` for fetch and push. Open **http://127.0.0.1:5050**. Expect three choices and **“Starter: game rules not built yet.”** Click a choice: no winner is expected yet. Leave this terminal running; code edits reload automatically.

Open a second terminal in this project folder for the remaining commands. Open this same folder as a local project in Codex. Stuck? [Setup help](https://kaw393939.github.io/218_spec/setup.html). Already have your copy running? Continue below; do not create another copy.

## 2. Decide what to build

Open `SPEC.md` in VS Code and attach it in ChatGPT desktop. Ask:

> Help me understand RPS-001. Do not code. Explain what the player should see and how we will check it. Help me clarify the short plan without adding features.

Read the nine-matchup table yourself. Whose perspective does “win” mean? Ask about anything unclear. Keep scoring for later. Save the agreed plan in **SPEC.md → Agreed plan**, replacing that section's starter text in VS Code. Carry the decisions, not the whole conversation.

In **your repository → Issues → New issue**, create **“RPS-001: Play a round”**. Use this short body, adjusting it to your agreed plan:

> Implement RPS-001 in SPEC.md. Show both choices and the correct result. A new choice starts another independent round. Check all nine matchups and one complete submitted round. No scoring yet.

Copy the issue URL into **SPEC.md → Work record**.

## 3. Build and let AI check first

In the second terminal:

```sh
git status --short --branch
git switch -c rps-001
```

Expect `## main...origin/main` and only your intended `SPEC.md` edit. If the branch already exists, use `git switch rps-001`.

In Codex, with **your cloned folder** open, ask:

> Read AGENTS.md and SPEC.md. Explain your plan and flag conflicts before coding. After I approve, implement only RPS-001 in game.py. Add tests/test_game.py with the nine explicit expected outcomes from the spec and one real request/result integration check with a fixed computer choice. Run .venv/bin/python -m pytest. Review your diff against the spec and fix problems you find. Report what you actually tested and what still needs a human check. Do not commit or push.

Read its plan before approving. Supplied tests check the shell, **not the missing rules**. New tests should use the table's answers, not calculate expected answers with the winner function.

## 4. Play, inspect, and give feedback

Refresh the local game. Play several rounds: do both choices and the result make sense? Can you choose again? Try Tab and Enter too.

In the second terminal:

```sh
.venv/bin/python -m pytest
git diff
```

Press `q` if Git opens a scrolling view. Open `game.py` and `tests/test_game.py` in VS Code. Ask AI to explain one winning case and its test. Random clicking cannot reliably cover all nine matchups; deterministic tests do that.

Tell Codex what you actually saw. For a problem, describe what you did, expected, and saw; ask for a focused fix and retest. Ask it to update **SPEC.md → Work record** with actual checks and links to `game.py` and `tests/test_game.py`. Do not claim checks nobody performed.

## 5. Keep the reviewed change

Expect changes to `game.py`, `tests/test_game.py`, and `SPEC.md`. Ask about any other changed files before keeping them.

```sh
git add game.py tests/test_game.py SPEC.md
git diff --cached
git commit -m "RPS-001: play a round"
git push -u origin rps-001
```

In **your repository → Pull requests → New pull request**, use base `main` and compare `rps-001`. Briefly describe the result and actual checks. Include **`Closes #N`** with your issue number. Inspect **Files changed**, wait for **Python checks** to pass, then merge when it matches the spec. Deploying a website is not part of this exercise.

**Done:** the game works locally, the PR is merged, its issue is closed, and the spec links to code and actual checks. Stop the server with Ctrl+C. You should be able to point to a rule, its code, and evidence that it works.

**Next time:** [RPS-002: first to two wins](NEXT.md). Keep that separate from your first PR.

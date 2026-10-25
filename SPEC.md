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

Replace this paragraph with your short plan after discussing it with ChatGPT. Keep the nine expected results above. Resolve questions before asking Codex to implement them.

### Checks

AI runs nine explicit rule cases plus a complete submitted round with a fixed computer move, then reviews the diff against this spec. The student plays, inspects a rule and its test, and gives feedback. Passing rule tests alone does not establish that the browser is usable or every control is wired correctly.

### Work record

- Issue: add your own issue URL.
- Implementation: **Not implemented.** The shell is supplied; `game.py` is unfinished.
- Checks: **Rules not verified.** Supplied tests cover the shell only. Record actual AI checks and your browser observations here after implementation; put detailed results in the PR.

"""Player-perspective rules for one independent Rock, Paper, Scissors round."""


def determine_winner(player: str, computer: str) -> str:
    """Return win, lose, or tie for two validated lowercase moves."""
    if player == computer:
        return "tie"
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "win" if beats[player] == computer else "lose"

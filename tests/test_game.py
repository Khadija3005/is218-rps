"""Explicit rules and real request/result checks for RPS-001."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_nine_outcomes(player, computer, expected):
    """Every valid pair has its literal player-perspective result."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_real_losing_round(monkeypatch):
    """The real route and rules display rock losing to paper."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert 'data-outcome="lose"' in html
    assert "Computer wins" in html
    assert "Rock" in html and "Paper" in html
    assert "You chose" in html and "Computer chose" in html
    assert "game rules not built yet" not in html

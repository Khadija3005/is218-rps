"""Completed rounds and independent keyboard replay through real HTTP."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_round_and_replay(page: Page, live_server, monkeypatch):
    """Rock loses to paper, then scissors wins a fresh keyboard round."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    page.goto(live_server)
    page.get_by_role("button", name="Rock", exact=True).click()
    choices = page.get_by_label("This round’s choices")
    expect(choices.locator(".choice-value")).to_have_text(["Rock ✊", "Paper ✋"])
    expect(
        page.get_by_role("heading", name="Computer wins", exact=True)
    ).to_be_visible()
    expect(page.locator(".result")).to_have_attribute("data-outcome", "lose")
    page.get_by_role("button", name="Paper", exact=True).focus()
    page.keyboard.press("Tab")
    expect(page.get_by_role("button", name="Scissors", exact=True)).to_be_focused()
    page.keyboard.press("Enter")
    expect(choices.locator(".choice-value")).to_have_text(["Scissors ✌", "Paper ✋"])
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_be_visible()
    expect(page.locator(".result")).to_have_attribute("data-outcome", "win")
    expect(page.locator(".choices")).to_have_count(1)

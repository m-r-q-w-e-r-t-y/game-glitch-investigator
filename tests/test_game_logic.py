from logic_utils import (
    check_guess,
    get_hint_message,
    get_range_for_difficulty,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# --- Bug fix regression tests ---

def test_hint_message_not_reversed_when_too_high():
    # BUG 1 FIX: guessing above the secret must tell the player to go LOWER
    outcome = check_guess(60, 50)
    message = get_hint_message(outcome)
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_hint_message_not_reversed_when_too_low():
    # BUG 1 FIX: guessing below the secret must tell the player to go HIGHER
    outcome = check_guess(40, 50)
    message = get_hint_message(outcome)
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_attempt_count_not_off_by_one():
    # BUG 3 FIX: the first attempt should score as attempt 1, not attempt 2,
    # so a first-try win should award 90 points, not 80.
    score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert score == 90

def test_get_range_for_difficulty_matches_selected_difficulty():
    # Supports BUG 2 FIX: "New Game" must regenerate the secret using the
    # selected difficulty's range instead of a hardcoded 1-100 range.
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Normal") == (1, 100)

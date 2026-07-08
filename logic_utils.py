"""Core game logic for the Number Guessing Game.

These functions are pure (no Streamlit / session_state dependency) so they
can be unit tested in isolation from the UI in app.py.
"""


def get_range_for_difficulty(difficulty: str):
    """Return the (low, high) inclusive guessing range for a difficulty.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard".

    Returns:
        A tuple (low, high). Unknown difficulties default to (1, 100).
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse raw text input into an integer guess.

    Args:
        raw: The raw text entered by the player.

    Returns:
        A tuple (ok, guess_int, error_message). When parsing fails, ok is
        False, guess_int is None, and error_message explains why.
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """Compare a guess to the secret number.

    Args:
        guess: The player's guess.
        secret: The correct number.

    Returns:
        "Win" if the guess matches, "Too High" if the guess is above the
        secret, or "Too Low" if the guess is below the secret.
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def get_hint_message(outcome: str):
    """Return the player-facing hint text for a given outcome.

    # FIX: The original app.py swapped these two messages, so a guess
    # above the secret ("Too High") told the player to "Go HIGHER" and a
    # guess below the secret ("Too Low") told them to "Go LOWER" -- the
    # exact opposite of correct advice. This mapping is now correct.

    Args:
        outcome: "Win", "Too High", or "Too Low".

    Returns:
        A short message string for display to the player.
    """
    messages = {
        "Win": "🎉 Correct!",
        "Too High": "📉 Go LOWER!",
        "Too Low": "📈 Go HIGHER!",
    }
    return messages.get(outcome, "")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the running score based on the outcome of a guess.

    Args:
        current_score: The score before this guess.
        outcome: "Win", "Too High", or "Too Low".
        attempt_number: The 1-based number of this attempt.

    Returns:
        The updated score.
    """
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

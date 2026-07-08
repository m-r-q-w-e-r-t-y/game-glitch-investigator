# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   - The purpose of the game is to guess a number from 1-100 that the code has randomly picked.
- [ ] Detail which bugs you found.
   1. Bug 1: "Go Lower" / "Go Higher" is flipped. Suppose the secret is 90, submitting 80 yields "Go Lower" and submitting 100 yields "Go Higher". It should be the opposite.
   2. Bug 2: Clicking "New Game" does not start a new game. To play again, you need for refresh the page.
   3. Bug 3: The player gets 1 less attempt then expected. For example, given 7 attempts, the system only allows 6. 
- [x] Explain what fixes you applied.
   1. **Bug 1 (hints reversed):** Added `get_hint_message()` in `logic_utils.py` with the correct outcome-to-message mapping, so "Too High" now says "Go LOWER" and "Too Low" now says "Go HIGHER".
   2. **Bug 2 (New Game didn't reset):** The "New Game" button in `app.py` now resets `status`, `score`, and `history` in addition to `attempts` and `secret`, and regenerates the secret using the selected difficulty's range instead of a hardcoded 1-100.
   3. **Bug 3 (off-by-one attempts):** `st.session_state.attempts` now initializes to `0` instead of `1`, so "attempts left" and the scoring formula in `update_score()` line up with the actual number of guesses made.

## 📸 Demo Walkthrough

1. Difficulty is set to "Normal" (secret is between 1 and 100).
2. User enters a guess of 40 → hint shows "📈 Go HIGHER!"
3. User enters a guess of 70 → hint shows "📉 Go LOWER!"
4. Score updates after each guess (points deducted for missed guesses).
5. User enters the correct number → "🎉 Correct!" is shown, balloons appear, and the game reports the final score.
6. Clicking "New Game 🔁" immediately starts a fresh round with a new secret, a reset score, and full attempts restored (previously this required a manual page refresh).

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest tests/ -v
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0
rootdir: .../ai110-module1show-gameglitchinvestigator-starter-main
collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_hint_message_not_reversed_when_too_high PASSED [ 57%]
tests/test_game_logic.py::test_hint_message_not_reversed_when_too_low PASSED [ 71%]
tests/test_game_logic.py::test_attempt_count_not_off_by_one PASSED       [ 85%]
tests/test_game_logic.py::test_get_range_for_difficulty_matches_selected_difficulty PASSED [100%]

============================== 7 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

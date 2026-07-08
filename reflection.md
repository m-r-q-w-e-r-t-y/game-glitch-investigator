# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game looked playable at first glance — a number input, a submit button, and a hint message — but it quickly became clear the hints, the "New Game" button, and the attempt count were all broken, making the game frustrating or impossible to actually win.

Two concrete bugs noticed right away: the "Go Higher/Go Lower" hints were backwards, and clicking "New Game" didn't actually reset the game (the page had to be refreshed instead).

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret is 90; guess 80 | "Go Higher" (80 is below 90) | Shows "Go Lower" | None — silent logic bug in `check_guess` |
| Secret is 90; guess 100 | "Go Lower" (100 is above 90) | Shows "Go Higher" | None — silent logic bug in `check_guess` |
| Click "New Game" after a round ends | A fresh secret number and reset attempts/status so play can continue | Attempts/secret reset internally, but the game still shows "Game over" / "You already won" and won't accept guesses; page refresh is required | None — silent state bug (`status` not reset) |
| Difficulty set to allow 7 attempts, then play a full round | Player gets 7 guesses before losing | Game ends after 6 guesses | None — off-by-one in the attempts counter |

---

## 2. How did you use AI as a teammate?

I used Claude (via Cowork) as my AI coding assistant throughout this project, attaching `app.py` and `logic_utils.py` so it had context on both the UI and logic layers.

**Correct suggestion:** When I described the hint bug, Claude correctly traced it to the `check_guess` function in `app.py` — it identified that the outcome labels ("Too High"/"Too Low") were correct, but the *messages* attached to them were swapped, so a guess above the secret said "Go HIGHER" instead of "Go LOWER". I verified this by manually tracing the code with secret=90, guess=100 (guess > secret) and confirming it printed "Go HIGHER" — the opposite of correct advice. The fix (a corrected `get_hint_message` mapping) resolved it, confirmed by the `test_hint_message_not_reversed_*` tests passing.

**Incorrect/misleading suggestion:** Claude's first pass at refactoring `check_guess` kept the original `try/except TypeError` fallback that compared the guess and secret as strings when a `TypeError` was raised. This looked like defensive coding, but it was actually masking a separate bug in `app.py` where the secret was silently converted to a string on every even-numbered attempt, causing guesses to be compared lexicographically instead of numerically (e.g., `9 > "10"` evaluates true as strings). I verified this by testing a guess of 9 against a secret of 10 on an even attempt and seeing "Too High" instead of "Too Low". I rejected keeping the fallback and instead removed the string-conversion bug at its source in `app.py`, since silently swallowing a real type error was hiding a bug rather than fixing one.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only once both a targeted `pytest` test and a manual run of the live Streamlit app confirmed the corrected behavior — a passing unit test alone wasn't enough, since some bugs (like the New Game reset) only show up in `session_state` across reruns. I ran `python -m pytest tests/ -v` after each fix; for example, `test_attempt_count_not_off_by_one` asserts that a first-attempt win awards 90 points instead of the old (buggy) 80, which confirmed the off-by-one in `update_score` was resolved. I also manually played a full round in the browser after each fix — winning, losing, and clicking "New Game" — to make sure nothing crashed and the fixed behavior matched what the tests claimed. AI helped me design the new tests by suggesting assertions that isolate each bug (e.g., checking for the string "LOWER" vs "HIGHER" in the hint message) rather than just re-testing the happy path.

---

## 4. What did you learn about Streamlit and state?

Streamlit re-runs your entire script from top to bottom every time you interact with a widget (like clicking a button or typing in a text box) — it's not like a normal event-driven app where only a small handler function runs. Because of that full rerun, any variable you want to "remember" between interactions (like the secret number, score, or attempt count) has to be stored in `st.session_state`, which persists across reruns instead of resetting. This project's "New Game" bug was a great example of *why* that matters: I reset some session_state values but forgot others (`status`), so the very next rerun re-read the stale `status` value and blocked the new game before it could start.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing a small regression test immediately after fixing each bug, named after the bug it targets (e.g., `test_attempt_count_not_off_by_one`) — it made it obvious what each test was protecting against and gave me fast, repeatable proof the fix actually worked. Next time, I'd ask my AI assistant to explain *why* a suggested fix works (not just accept the diff) before applying it, since one "defensive" fallback it suggested was actually hiding a separate bug instead of solving one. This project changed how I think about AI-generated code mainly by showing that AI can produce code that runs without erroring while still being logically wrong in subtle ways — passing test coverage and manual verification are what actually caught the real bugs, not just the absence of a crash.

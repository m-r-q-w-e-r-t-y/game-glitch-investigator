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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

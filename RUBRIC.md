### Project 1: Game Glitch Investigator

Total Points: **18pts** + 10pts bonus

## Required Features

| 3pts | Bug Reproduction Evidence |
|---|---|
|  | There is a written trace or terminal output (in a markdown code block or committed text file) documenting that the game was run, referencing specific game events. |
|  | Two or more incorrect behaviors, each tied to a specific input/trigger and its observed (incorrect) output (e.g., a Bug Reproduction Logs table row), not merely named. |
|  | Each documented bug specifies expected vs actual behavior (e.g., "Score never increases when collecting items," "Game crashes on arrow-key input due to missing boundary check") — an entry giving only the actual result does not count. |

| 3pts | Identification of At Least Three Distinct Bugs |
|---|---|
|  | There are three or more distinct bugs or issues listed (a count only — whether each is a real starter bug is judged separately below). |
|  | The bug descriptions correctly identify code-level causes or problematic sections. |
|  | All bugs are real, reproducible issues present in the starter code. |

| 3pts | Verification and Critique of AI Debugging Suggestions |
|---|---|
|  | There is at least one AI-generated explanation of a bug. |
|  | At least one correct AI suggestion is identified and explained why it is correct. |
|  | At least one incorrect or misleading AI suggestion is identified and explained why it is not correct. |

_Documented in `reflection.md` section 2 — the optional `ai_interactions.md` stretch log does not count toward this criterion._

| 3pts | Implementation of At Least Two Correct Bug Fixes |
|---|---|
|  | At least two of the documented bugs are fixed. |
|  | The fix(es) made resolve their issue(s) without introducing regressions (awarded even for a single clean fix; a partial fix that leaves a related issue does not count). |
|  | There is an explanation of what is changed to fix the bug and why the fix works (award for any fix actually made, even if only one bug was fixed). |

| 3pts | Working Game Demonstration (Post-Fix) |
|---|---|
|  | There is text-based evidence the game runs without crashing after updates — passing pytest output, terminal output in a markdown code block, or a written markdown walkthrough of a game session. |
|  | The game behavior matches the intended function for the fixed issues. |
|  | There are no new critical errors introduced. |

| 3pts | Documentation, Reflection, and Git Usage |
|---|---|
|  | README clearly describes the game's purpose, bugs found, and fixes applied. |
|  | Reflection summarizes AI collaboration, including both helpful and flawed AI outputs. |
|  | Git history includes 3 or more commits with unique messages (not one bulk commit) — counted mechanically; commit content/intent is not judged. |

## Stretch Features

| +2pts | Advanced Edge-Case Testing |
|---|---|
|  | At least three pytest cases targeting complex edge cases (e.g., handling non-numeric strings, negative numbers, or empty inputs) are implemented. |
|  | Tests are specific and pass successfully. Terminal output showing all tests passing is pasted as a fenced code block in the README. |
|  | `ai_interactions.md` records the test-generation prompt(s) and a short rationale for each edge case chosen. |

| +2pts | Feature Expansion via Agent Mode |
|---|---|
|  | Agent Mode is used to implement a meaningful new feature (e.g., a "High Score" tracker, "Guess History" sidebar, or "Difficulty Levels"). The feature is fully functional. |
|  | `ai_interactions.md` includes an "Agent Workflow" section documenting: files modified, task requested of the agent, what the agent completed, and any manual corrections made. |

| +2pts | Professional Documentation and Style |
|---|---|
|  | AI assistance is used to add professional docstrings to all functions in logic_utils.py. |
|  | Code follows PEP 8 style guidelines, and `ai_interactions.md` includes the prompt(s) used, the linting output (code block or committed `.txt`), and notes on what formatting/naming changes the AI suggested and which were applied. |

| +2pts | Enhanced Game UI and Formatting |
|---|---|
|  | Student adds structured, user-friendly output to the game (e.g., color-coded hints, emojis for "Hot/Cold" states, or a summary table of the game session). |
|  | Formatting significantly improves the player experience without breaking core game logic. |
|  | README includes a description of the UI enhancements and references the relevant code (e.g., function names modified). |

| +2pts | Thorough AI Model or Prompt Comparison |
|---|---|
|  | `ai_interactions.md` includes a section comparing the output of two different models (e.g., Copilot GPT-4o vs. Gemini) for a specific logic bug. |
|  | Analysis includes which model provided a more "Pythonic" fix and which explanation was easier to understand. |

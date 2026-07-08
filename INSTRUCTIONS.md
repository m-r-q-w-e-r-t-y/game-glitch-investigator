[](#feedback-modal)

📬 Reminder: Project 1 is due by **Monday, June 22nd at 2:59AM EDT**.

[](#heading-show-what-you-know-game-glitch-investigator)Show What You Know: Game Glitch Investigator
----------------------------------------------------------------------------------------------------

### [](#heading-project-overview)ℹ️ Project Overview

**⏰ ~3 hours**

Your AI pair programmer decided to be helpful and built you a Python game. Only problem? It's full of glitches. Sometimes the game never ends, the hints lie, or the score goes haywire. Your mission: become the **Game Glitch Investigator** -- a developer who can diagnose, explain, and repair AI-generated code responsibly. You'll use your AI coding assistant to find bugs, plan refactors across multiple files, and generate automated tests.

#### [](#heading-goals)🎯 Goals

By completing this project, you will be able to...

*   Identify syntax, logic, and runtime bugs in AI-generated Python code.
    
*   Use AI tools critically to propose, test, and verify debugging solutions.
    
*   Apply readable, testable fixes while using AI to generate `pytest` cases for verification.
    
*   Reflect on human judgment, identifying when to accept, modify, or reject AI-generated plans and code.
    

* * *

### [](#heading-project-instructions)✏️ Project Instructions

Phase 1: Glitch Hunt

**⏰ ~45 mins**

In this phase, you'll fork and set up your project, run the buggy game, and investigate what's going wrong. Your goal is to observe, record, and reason — not to fix yet — so you can understand how the game behaves and where the AI's logic starts to break down.

**Setup: Get Your Starter Code**

*   Go to the [**Game Glitch Investigator**](https://github.com/codepath/ai110-module1show-gameglitchinvestigator-starter) repo.
    
*   Click **Fork** to create your own copy under your GitHub account.
    
*   Clone the fork to your computer, then open the cloned folder in VS Code.
    

* * *

**Step 1: Run and Observe**

*   Find the file named `app.py`.
    
*   Install the required libraries by typing `pip install -r requirements.txt` in your terminal.
    
*   Run the game by typing `python -m streamlit run app.py` in your terminal.
    
*   Play the game at least twice using different inputs. Watch what happens carefully! Note any crashes, strange outputs (like hints that don't match your guess), or disappearing scores.
    
    Think you're running into bugs before you should? Use this [Getting Started video](https://www.loom.com/share/f5f84df907c7447dacb723f959bb812a) as a sanity check that what you're seeing is intended!
    

* * *

**Step 2: Document the Glitches**

*   Identify at least three bugs or issues you noticed while playing.
    
*   Open the `reflection.md` file.
    
*   Use the section **1\. What was broken when you started?** to document these bugs. For each, describe what you expected to happen versus what actually happened.
    
*   In the same section, create a **Bug Reproduction Logs** markdown table documenting at least 3 reproducible bug cases. Each row should capture:
    
    Input Used
    
    Expected Behavior
    
    Actual Behavior
    
    Console Error / Output
    
    (e.g., guess of 60)
    
    (e.g., "Too High" hint)
    
    (e.g., "Too Low" hint shown)
    
    (paste any error text, or "none")
    
    This table gives a clear, text-based record of each bug that anyone (or any tool) can read without watching you play.
    

* * *

**Step 3: Ask AI for Help**

*   Open your AI coding assistant in VS Code.
    
*   Attach the relevant files (e.g., `app.py` and `logic_utils.py`) to give the AI context of your project code.
    
    If you aren't sure why a specific line is there, highlight it and use your AI coding assistant's chat (Cmd+I / Ctrl+I) to ask: "Explain this logic step-by-step."
    
*   Describe one specific glitch you found and ask the AI to explain the underlying logic causing it.
    

📍**Checkpoint**: You've forked the repo, successfully run the app via Streamlit, identified three clear issues in `reflection.md`, and used your AI coding assistant's workspace awareness to understand the buggy logic.

 Close Section

Phase 2: Investigate and Repair

**⏰ ~60 mins**

Now that you know what's broken, it's time to start fixing it -- thoughtfully. You'll use AI tools to help you test ideas, repair code across files, and verify that your game finally works as intended. The focus is on slow, careful debugging and documenting how you and the AI each contributed to the solution.

**Step 1: Target and Plan Your Fixes**

*   Look back at the three bugs you identified in Phase 1. Choose **two** to fix first.
    
*   In your code (`app.py` or `logic_utils.py`), add a comment like `# FIXME: Logic breaks here` where you believe the issue is located.
    
    Marking the "crime scene" in your code gives you a specific point to reference when using **your AI coding assistant's chat**.
    
*   For each bug, start a **new chat session** in your AI coding assistant's chat view to keep the AI focused on one problem at a time.
    
*   Attach the relevant files (e.g., `app.py`, `logic_utils.py`) or reference your codebase to ensure your AI coding assistant sees the relationship between your UI and logic files.
    

* * *

**Step 2: Refactor and Fix**

*   The starter code often mixes game logic with UI code in `app.py`. Use your AI coding assistant to refactor core logic (like `check_guess` or `parse_guess`) into `logic_utils.py`.
    
    Give a multi-step instruction like: "Move the `check_guess` function to `logic_utils.py`, update the logic to fix the high/low bug, and update the import in `app.py`.
    
*   When your AI coding assistant applies edits directly, you must carefully review the **diff** (the comparison of old vs new code) for every file it touched.
    
    If the changes look wrong or too complex, don't be afraid to click "Undo" or "Discard" and try again with a more specific prompt.
    
*   If the fix is 90% correct but has a small error, highlight that specific line and use your AI coding assistant's chat to ask for a targeted correction.
    

* * *

**Step 3: Test-Driven Verification**

*   Ask your AI coding assistant to generate a `pytest` case in `test/test_game_logic.py` that specifically targets the bug you just fixed.
    
*   Open your terminal and run `pytest`. Confirm that your new test passes along with the existing starter tests.
    
    A good test is simple. For example, if you fixed a "Too High" hint, your test should verify that a guess of `60` against a secret of `50` returns the "Too High" outcome.
    
*   Run the app with `streamlit run app.py` to confirm the fix works in the live game.
    

* * *

**Step 4: Document Your Work**

*   Near each fix in your code, add a short comment explaining how you and the AI collaborated (e.g., `#FIX: Refactored logic into logic_utils.py using agent mode`).
    
*   Open `reflection.md`.
    
*   Use the section **2\. How did you use AI as a teammate?** to document two types (correct and incorrect/misleading) of AI suggestions you received. For each, clearly explain:
    
    *   What the AI suggested.
        
    *   Whether the suggestion was correct or incorrect/misleading.
        
    *   How you verified the result in the code or game.
        
    
*   Use the section **3\. Debugging and testing your fixes** to record how you verified your repairs.
    
*   Ask your AI coding assistant to generate a commit message in the Source Control tab to create a clear summary of your repair.
    
*   Push your changes: `git push origin main`.
    

📍**Checkpoint**: Your game now runs smoothly! You have moved core logic into `logic_utils.py`, added at least one new automated test, and documented your AI collaboration process directly in the code.

 Close Section

Phase 3: Reflection and README

**⏰ ~30 mins**

In this final phase, you'll pull everything together -- your fixed game, your debugging notes, and your insights about working with AI. You'll finalize your documentation to explain what you did and capture what you learned about both the code and the AI-assisted debugging process.

**Step 1: Finalize your README**

*   Open `README.md`.
    
*   Update the **"Demo"** section. Instead of a screenshot or recording, write a textual **Demo Walkthrough** that steps through a sample game in order. For example:
    
        ## Demo Walkthrough
        1. User enters a guess of 40
        2. Game returns "Too Low"
        3. User enters a guess of 70 → "Too High"
        4. Score updates correctly after each guess
        5. Game ends after the correct guess
        
    
    This gives a clear, text-based record of how the game behaves end-to-end that anyone can follow without running it.
    
*   Fill in the **"Document Your Experience"** section.
    
*   If you completed **Challenge 1: Advanced Edge-Case Testing**, paste the terminal output showing your `pytest` results as a fenced code block in your `README.md`.
    

* * *

**Step 2: Write Your Reflection**

*   Open `reflection.md`.
    
*   Complete the final reflection questions in the file.
    
    Be honest! If the AI gave you a bad suggestion that you had to reject, explain why. This shows you were in control of the process, not just following the AI blindly.
    

* * *

**Step 4: Final Commit and Push**

*   Ask your AI coding assistant to generate a commit message to summarize your final documentation updates.
    
*   Send your completed project to GitHub:
    
    *   `git add .`
        
    *   `git commit -m "docs: finalized README and reflection"`
        
    *   `git push origin main`
        
    
    **Your commit history is graded.** As you work through the phases, commit your progress in **at least 3 separate commits with unique messages** (for example: one after logging the bugs, one after applying your fixes, one after finishing your README and reflection). A single bulk commit at the end will not earn the git-history point.
    

📍**Checkpoint**: You've completed your first AI-assisted debugging project! Your game runs clearly, your documentation tells the story of your reasoning, and your reflection shows how you grew as an AI-aware engineer.

 Close Section

Optional Extensions

**⏰ ~15-30 mins**

After completing your main debugging work, you can choose one short extension to deepen your technical reasoning. Each option builds an authentic engineering skill while giving you a chance to explore how AI fits into real-world development habits. These are optional but strongly encouraged if you finish early or want to strengthen your portfolio evidence.

Try one of the following to stretch your reasoning:

*   **Challenge 1: Advanced Edge-Case Testing**
    
    *   In Phase 2, you wrote a basic test. For this challenge, use your AI coding assistant to identify three potential "edge case" inputs (e.g., negative numbers, decimals, or extremely large values) that might still break your game.
    *   Use your AI coding assistant to generate a suite of `pytest` cases that verify your game handles these inputs gracefully.
    *   Paste the terminal output showing all tests passing as a **fenced code block** in your `README.md` (not a screenshot).
    *   In `ai_interactions.md`, record the prompt(s) you used to generate the tests and a one-line explanation of why each edge case was chosen.
    
*   **Challenge 2: Feature Expansion**
    
    *   Use your AI coding assistant agentically to plan and implement a meaningful new feature, such as a "High Score" tracker that saves your best score to a file or a "Guess History" sidebar that visualizes how close your previous guesses were.
    *   Add an **"Agent Workflow"** section to your `ai_interactions.md` documenting: which files were modified, what you asked the agent to do, what it completed, and any manual corrections you made.
    
*   **Challenge 3: Professional Documentation and Linting**
    
    *   Use your AI coding assistant to add professional-grade docstrings to every function in `logic_utils.py`.
    *   Then, ask your AI coding assistant to review your code for PEP 8 style compliance and apply its suggestions to resolve any formatting or naming issues it identifies.
    *   In `ai_interactions.md`, include the prompt(s) you used, paste the linting output (in a code block or committed `.txt`), and add a short note on what formatting/naming changes the AI suggested and which you applied.
    
*   **Challenge 4: Enhanced Game UI**
    
    *   Add structured and user-friendly output to the game such as color-coded hints, emojis for "Hot/Cold" states, or a summary table of the game session (without breaking core game logic).
    *   In your `README.md`, include a description of the UI enhancements you added and reference the relevant functions or code sections (e.g., which function was modified and what it now outputs).
    
*   **Challenge 5: AI Model Comparison**
    
    *   Take one of the logic bugs you found in Phase 1 and ask for a fix from two different models (e.g., Claude vs. Gemini, or ChatGPT vs. Copilot).
    *   In `ai_interactions.md`, add a comparison section covering each model: which one gave a more readable / more "Pythonic" fix, and which explained the "why" more clearly.
    

📍**Checkpoint**: You've leveled up from fixing bugs to thinking like a true engineer! Your game now runs cleanly, your reasoning is sharper, and your debugging process reflects real-world AI collaboration.

 Close Section

### [](#heading-required-files)📁 Required Files

Before submitting, confirm your repository includes the following:

*   `README.md` — project overview, Demo Walkthrough, and (if applicable) test output
*   `reflection.md` — bug reproduction logs and your AI collaboration reflection
*   `tests/test_game_logic.py` — your automated tests
*   `ai_interactions.md` — required only if you completed a stretch challenge that documents AI prompts, agent workflow, linting evidence, or a model comparison
*   `test_results.txt` _(optional)_ — generated via `pytest > test_results.txt`
*   `architecture.mmd` _(optional)_ — only if you created a diagram

### [](#heading-submitting-your-project)📬 Submitting Your Project

Once you've completed all the required features for your project, use the following checklist to prepare your work for submission.

1.  Code is pushed to the correct GitHub repository
2.  Repo is public
3.  Required files are present (code, README, reflection, tests if applicable)
4.  Commit history shows multiple meaningful commits
5.  Reflection answers the prompts with specific, honest details
6.  Final changes are committed and pushed before the deadline
7.  Submit your assignment using the submit button in Week 3.

* * *

### [](#heading-how-its-graded)🗺️ How It's Graded

_A detailed breakdown of graded features and points can be found on the course [grading](../pages/grading#heading-project-1-game-glitch-investigator) page._
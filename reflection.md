# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  Game started with 7 guesses instead of 8. Guessing button is glitchy. Incorrectly submits the incorrect number or requires more than one click to submit. The game gives incorrect hints. The game generates a number that is not in range of difficulty. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code for this project. It correctly identified several bugs in our code and I verified this by comparing the AI's list with my me and my teammates' list. The AI did claim that all bugs were found but there were some that weren't found that we noticed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

To determine if a bug was really fixed, I tested them in the client by running the game and trying the scenarios that originally caused the issue. For example, I entered invalid inputs like letters or empty guesses to make sure they no longer increased the attempt counter. This test showed that the input validation logic was working correctly. Claude Code also helped suggest cases to test, such as invalid input and out-of-range guesses, which I verified manually in the game.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because the original code had it regenerate a random number every click unconditionally. Streamlit reruns everytime the user clicks a button or changes an input. Session state is what saves values preventing it from being reset. To keep the secret number "stable", making sure it it changed when needed to.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to use in future projects is creating pytests to test code. One thing I would do different when I work with AI on a coding task is fixing bugs one by one and breaking down the bugs that needed to be fixed even more to follow along better and gain better control. This project changed how I think about working with AI as it feels more of a collaborative experience, especially when using Claude built into VS Code.

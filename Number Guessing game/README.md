
# 🎮 Number Guessing Game (Python CLI)

Welcome to the **Number Guessing Game**, a command-line Python game where you guess a number between 1 and 100 within a limited number of chances based on the selected difficulty.

---

## 🚀 Features

- ✅ Three difficulty levels:
  - **Easy** – 10 attempts
  - **Medium** – 5 attempts
  - **Hard** – 3 attempts
- ✅ Replayable — play multiple rounds without restarting
- ✅ ⏱️ Timer — tracks how long you take to guess the correct number
- ✅ 🏆 High Score — records your best (fewest attempts) for each difficulty
- ✅ 🎯 Clear feedback on each guess (too low / too high)

---

## 🧑‍💻 How to Run

### Requirements
- Python 3.x installed on your machine

### Run the game
```bash
python Guessing_game.py
````



---

## 📝 Example

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter Your choice: 2
Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 45
Incorrect! The number is greater than 45.

Enter your guess: 78
Incorrect! The number is less than 78.

...

Congratulations! You guessed the correct number in 4 attempts and 12.35 seconds.
🏆 New high score for Medium difficulty!
```

---

## 📦 File Structure

```
📁 Number-Guessing-Game
│
├── Guessing_game.py        # Main game file
├── README.md               # Game instructions and documentation
```

---

## 📌 Tips

* Type only numbers while guessing.
* To quit the game after any round, type `no` when prompted to play again.
* Your high scores are session-based and reset when you exit the program.

---

## 🧠 Future Ideas

* Persistent high scores using file storage
* Smarter hint system
* GUI-based version using Tkinter or PyQt

---

## 👨‍💻 Author

**Asura King**
Made with 💻 in Python

---

## 📃 License

This project is licensed for educational and personal use.

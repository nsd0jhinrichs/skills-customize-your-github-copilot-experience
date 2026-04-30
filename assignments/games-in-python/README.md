# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. In this assignment, you will practice managing game state, checking guesses, and guiding the player through a complete game.

## 📝 Tasks

### 🛠️	Create the Core Game Loop

#### Description
Write a Python program that chooses a secret word from a predefined list and lets the player guess one letter at a time. After each guess, the program should show the current progress of the word and keep the game running until the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list of possible words
- Ask the player to enter one letter guess at a time
- Show the current word progress using underscores for missing letters
- Track how many incorrect guesses the player has left
- End the game when the full word is guessed or no attempts remain


### 🛠️	Add Clear Game Feedback

#### Description
Improve the game so the player can easily understand what is happening after each turn. Display helpful messages for correct and incorrect guesses and show a final win or loss message when the game ends.

#### Requirements
Completed program should:

- Tell the player whether each guess was correct or incorrect
- Prevent the game from crashing when the player enters unexpected input
- Show the letters or word progress after every turn
- Display a clear winning message when the player guesses the word
- Display a clear losing message that reveals the secret word when attempts run out

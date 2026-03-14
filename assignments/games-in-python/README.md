
# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, and user input to practice fundamental programming concepts.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the game by creating a list of words and randomly selecting one for the player to guess.

#### Requirements
Completed program should:

- Define a list of words to choose from
- Randomly select a word for the game
- Initialize game state (guessed letters, attempts remaining)

### 🛠️ Guess Handling and Progress Display

#### Description
Implement the core game loop that accepts letter guesses, updates the game state, and displays current progress.

#### Requirements
Completed program should:

- Accept single letter guesses from the user
- Show current progress with underscores for unguessed letters (e.g., _ _ _ _)
- Track incorrect guesses and remaining attempts
- Prevent guessing the same letter twice

### 🛠️ Win/Lose Conditions and Messages

#### Description
Add logic to check for win/lose conditions and display appropriate messages when the game ends.

#### Requirements
Completed program should:

- End the game when the word is fully guessed or attempts are exhausted
- Display a win message with the correct word when player succeeds
- Display a lose message revealing the word when attempts run out

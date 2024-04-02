import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.max_attempts = 6
        self.current_word = ''
        self.guessed_letters = []
        self.remaining_attempts = self.max_attempts

    def select_word(self):
        self.current_word = random.choice(self.words).lower()

    def display_word(self):
        displayed_word = ''
        for letter in self.current_word:
            if letter in self.guessed_letters:
                displayed_word += letter + ' '
            else:
                displayed_word += '_ '
        return displayed_word.strip()

    def guess(self, letter):
        if letter in self.guessed_letters:
            print("You've already guessed that letter!")
            return

        self.guessed_letters.append(letter)

        if letter not in self.current_word:
            self.remaining_attempts -= 1
            print(f"Wrong guess! You have {self.remaining_attempts} attempts left.")
            if self.remaining_attempts == 0:
                print("Game over! The word was:", self.current_word)
                return False

        if self.display_word().replace(' ', '') == self.current_word:
            print("Congratulations! You guessed the word:", self.current_word)
            return False

        return True

def main():
    words = ["python", "hangman", "game", "programming", "computer"]
    game = Hangman(words)
    game.select_word()

    print("Welcome to Hangman!")
    print("The word has", len(game.current_word), "letters.")

    while True:
        print("Word:", game.display_word())
        letter = input("Guess a letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue
        if not game.guess(letter):
            break

if __name__ == "__main__":
    main()









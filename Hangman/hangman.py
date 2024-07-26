import random
import random
from countries_data import countries

def get_country(countries):
    word = random.choice(countries)
    return word.upper()

class HangmanGame:
    def __init__(self, word, max_lives=6):
        self.word = word
        self.guessed_letters = []
        self.lives = max_lives

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            return True
        elif letter not in self.word:
            self.lives -= 1
            return False
        return None

    def display_progress(self):
        return ' '.join([letter if letter in self.guessed_letters else '-' for letter in self.word])

    def is_finished(self):
        return self.lives <= 0 or set(self.word) == set(self.guessed_letters)

    def is_won(self):
        return set(self.word) == set(self.guessed_letters)

class HangmanUI:
    def __init__(self, game):
        self.game = game

    def start(self):
        print("Welcome to Hangman!", flush=True)
        while not self.game.is_finished():
            print("Current progress: ", self.game.display_progress(), flush=True)
            print(f"Lives left: {self.game.lives}", flush=True)
            guess = input("Guess a letter: ").upper()
            if guess and self.game.guess(guess):
                print("Good guess!", flush=True)
            else:
                print("Wrong guess or already guessed.", flush=True)
        
        if self.game.is_won():
            print("Congratulations! You guessed the word:", self.game.word, flush=True)
        else:
            print("You ran out of lives. The word was:", self.game.word, flush=True)


if __name__ == "__main__":
    word = get_country(countries)
    game = HangmanGame(word)
    ui = HangmanUI(game)
    ui.start()


def get_country(countries):
    word = random.choice(countries)
    return word.upper()

class HangmanGame:
    def __init__(self, word, max_lives=6):
        self.word = word
        self.guessed_letters = []
        self.lives = max_lives

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            return True
        elif letter not in self.word:
            self.lives -= 1
            return False
        return None

    def display_progress(self):
        return ' '.join([letter if letter in self.guessed_letters else '-' for letter in self.word])

    def is_finished(self):
        return self.lives <= 0 or set(self.word) == set(self.guessed_letters)

    def is_won(self):
        return set(self.word) == set(self.guessed_letters)

class HangmanUI:
    def __init__(self, game):
        self.game = game

    def start(self):
        print("Welcome to Hangman!")
        while not self.game.is_finished():
            print("Current progress: ", self.game.display_progress())
            print(f"Lives left: {self.game.lives}")
            guess = input("Guess a letter: ").upper()
            if guess and self.game.guess(guess):
                print("Good guess!")
            else:
                print("Wrong guess or already guessed.")
        
        if self.game.is_won():
            print("Congratulations! You guessed the word:", self.game.word)
        else:
            print("You ran out of lives. The word was:", self.game.word)


if __name__ == "__main__":
    word = get_country(countries)
    game = HangmanGame(word)
    ui = HangmanUI(game)
    ui.start()

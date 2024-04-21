import tkinter as tk
import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.selected_word = random.choice(words)
        self.word_length = len(self.selected_word)
        self.display = ['_'] * self.word_length
        self.tries = 6
        self.guessed_letters = set()
        self.game_over = False

        # Tkinter setup
        self.window = tk.Tk()
        self.window.title("Hangman")

        self.word_label = tk.Label(self.window, text=" ".join(self.display), font=("Arial", 24))
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.window, text="Guess", command=self.process_guess)
        self.guess_button.pack()

        self.status_label = tk.Label(self.window, text=f"Tries left: {self.tries}")
        self.status_label.pack()

    def get_valid_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)  # Clear entry
        if guess.isalpha():
            return guess
        else:
            self.status_label.config(text="Invalid input. Please enter letters only.")
            return None

    def show_result(self):
        self.word_label.config(text=" ".join(self.display))
        self.status_label.config(text=f"Tries left: {self.tries}")

    def process_guess(self):
        guess = self.get_valid_guess()
        if not guess or guess in self.guessed_letters:
            self.status_label.config(text="Invalid guess or already guessed.")
            return

        if guess in self.selected_word:
            self.guessed_letters.add(guess)
            # Reveal correctly guessed letters
            for i, letter in enumerate(self.selected_word):
                if letter == guess:
                    self.display[i] = guess
            if "_" not in self.display:
                self.game_over = True
                self.status_label.config(text="Best wishes! You guessed correctly.")
        else:
            self.tries -= 1
            self.guessed_letters.add(guess)
            if self.tries == 0:
                self.game_over = True
                self.status_label.config(text=f"You're out of chances. The word was: {self.selected_word}")
            else:
                self.status_label.config(text="Incorrect guess.")

        self.show_result()  # Update the GUI with the current state of the game

if __name__ == "__main__":
    my_words = ['psychology', 'math', 'geography', 'otorhinolaryngologist', 'logic', 'teacher']
    game = Hangman(my_words)
    game.window.mainloop()  # Start the Tkinter event loop

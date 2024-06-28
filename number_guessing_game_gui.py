import random
import tkinter as tk

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x200")

        self.mode_label = tk.Label(master, text="Select mode:")
        self.mode_label.pack()

        self.mode_var = tk.IntVar()
        self.easy_mode_radio = tk.Radiobutton(master, text="Easy Mode", variable=self.mode_var, value=1)
        self.easy_mode_radio.pack()
        self.hard_mode_radio = tk.Radiobutton(master, text="Hard Mode", variable=self.mode_var, value=2)
        self.hard_mode_radio.pack()

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.guess_label = tk.Label(master, text="")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.secret_number = None
        self.guesses_remaining = 0

    def start_game(self):
        mode = self.mode_var.get()
        if mode == 1:
            self.secret_number = random.randint(1, 100)
            self.guesses_remaining = float('inf')
            self.guess_label.config(text="Enter your guess (1-100):")
        elif mode == 2:
            self.secret_number = random.randint(1, 1000)
            self.guesses_remaining = 10
            self.guess_label.config(text="Enter your guess (1-1000):")
        else:
            self.result_label.config(text="Invalid mode selected")

    def check_guess(self):
        guess = int(self.guess_entry.get())
        if guess == self.secret_number:
            self.result_label.config(text="Congratulations, you guessed correctly!")
        elif guess > self.secret_number:
            self.result_label.config(text=f"The number is less than {guess}.")
            self.guesses_remaining -= 1
            if self.guesses_remaining > 0:
                self.guess_label.config(text=f"Enter your next guess ({self.guesses_remaining} remaining):")
            else:
                self.result_label.config(text="You ran out of guesses!")
        else:
            self.result_label.config(text=f"The number is greater than {guess}.")
            self.guesses_remaining -= 1
            if self.guesses_remaining > 0:
                self.guess_label.config(text=f"Enter your next guess ({self.guesses_remaining} remaining):")
            else:
                self.result_label.config(text="You ran out of guesses!")

    def create_widgets(self):
        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

root = tk.Tk()
my_game = NumberGuessingGame(root)
my_game.create_widgets()
root.mainloop()

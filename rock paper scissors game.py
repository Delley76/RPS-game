import tkinter as tk
from tkinter import font as tkfont
import random


# Yeah so this is my RPS game, kinda messy but it works lol
class Game:
    def __init__(self, window):
        self.window = window
        window.title("RPS Game")
        window.geometry("480x580")
        window.config(bg="#5a67d8")

        # keep track of wins
        self.my_wins = 0
        self.cpu_wins = 0

        # game stuff
        self.options = ['rock', 'paper', 'scissors']
        self.icons = {
            'rock': '✊',
            'paper': '✋',
            'scissors': '✌️'
        }

        self.build_interface()

    def build_interface(self):
        # top title thing
        big_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
        header = tk.Label(
            self.window,
            text="Rock Paper Scissors",
            font=big_font,
            bg="#5a67d8",
            fg="white"
        )
        header.pack(pady=25)

        # main container for everything
        container = tk.Frame(self.window, bg="white", bd=2, relief=tk.RIDGE)
        container.pack(padx=25, pady=15, fill=tk.BOTH, expand=True)

        # where the buttons go
        btn_area = tk.Frame(container, bg="white")
        btn_area.pack(pady=25)

        emoji_font = tkfont.Font(family="Helvetica", size=38)

        # make the three buttons
        for option in self.options:
            button = tk.Button(
                btn_area,
                text=self.icons[option],
                font=emoji_font,
                width=3,
                bg="#f7fafc",
                activebackground="#e2e8f0",
                command=lambda x=option: self.make_move(x)
            )
            button.pack(side=tk.LEFT, padx=12)

        # show results here
        results_area = tk.Frame(container, bg="white")
        results_area.pack(pady=25)

        outcome_font = tkfont.Font(family="Helvetica", size=17, weight="bold")
        self.outcome_text = tk.Label(
            results_area,
            text="Pick one to start!",
            font=outcome_font,
            bg="white",
            fg="#2d3748"
        )
        self.outcome_text.pack()

        detail_font = tkfont.Font(family="Helvetica", size=13)
        self.detail_text = tk.Label(
            results_area,
            text="",
            font=detail_font,
            bg="white",
            fg="#718096"
        )
        self.detail_text.pack(pady=8)

        # scoreboard section
        scores = tk.Frame(container, bg="white")
        scores.pack(pady=25, fill=tk.X)

        # my score
        my_section = tk.Frame(scores, bg="white")
        my_section.pack(side=tk.LEFT, expand=True)

        label_font = tkfont.Font(family="Helvetica", size=11)
        tk.Label(
            my_section,
            text="You",
            font=label_font,
            bg="white",
            fg="#718096"
        ).pack()

        num_font = tkfont.Font(family="Helvetica", size=30, weight="bold")
        self.my_score = tk.Label(
            my_section,
            text="0",
            font=num_font,
            bg="white",
            fg="#5a67d8"
        )
        self.my_score.pack()

        # computer score
        cpu_section = tk.Frame(scores, bg="white")
        cpu_section.pack(side=tk.RIGHT, expand=True)

        tk.Label(
            cpu_section,
            text="Computer",
            font=label_font,
            bg="white",
            fg="#718096"
        ).pack()

        self.cpu_score = tk.Label(
            cpu_section,
            text="0",
            font=num_font,
            bg="white",
            fg="#5a67d8"
        )
        self.cpu_score.pack()

        # reset button at bottom
        btn_font = tkfont.Font(family="Helvetica", size=11, weight="bold")
        reset = tk.Button(
            container,
            text="Start Over",
            font=btn_font,
            bg="#5a67d8",
            fg="white",
            activebackground="#4c51bf",
            padx=25,
            pady=12,
            command=self.start_over
        )
        reset.pack(pady=15)

    def make_move(self, my_pick):
        # computer picks randomly
        cpu_pick = random.choice(self.options)

        # figure out who won
        result = self.check_winner(my_pick, cpu_pick)

        # update everything
        self.show_result(my_pick, cpu_pick, result)
        self.add_points(result)

    def check_winner(self, mine, theirs):
        # tie case
        if mine == theirs:
            return 'draw'

        # check if I won
        winning_combos = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }

        if winning_combos[mine] == theirs:
            return 'win'
        else:
            return 'lose'

    def show_result(self, mine, theirs, result):
        # change message based on outcome
        messages = {
            'win': "Nice! You won!",
            'lose': "Computer won!",
            'draw': "Tie game!"
        }

        colors = {
            'win': "#48bb78",
            'lose': "#f56565",
            'draw': "#ed8936"
        }

        self.outcome_text.config(
            text=messages[result],
            fg=colors[result]
        )

        self.detail_text.config(
            text=f"You threw {self.icons[mine]} | Computer threw {self.icons[theirs]}"
        )

    def add_points(self, result):
        if result == 'win':
            self.my_wins += 1
            self.my_score.config(text=str(self.my_wins))
        elif result == 'lose':
            self.cpu_wins += 1
            self.cpu_score.config(text=str(self.cpu_wins))
        # don't add points for ties

    def start_over(self):
        # reset everything back to zero
        self.my_wins = 0
        self.cpu_wins = 0
        self.my_score.config(text="0")
        self.cpu_score.config(text="0")
        self.outcome_text.config(text="Pick one to start!", fg="#2d3748")
        self.detail_text.config(text="")


# run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
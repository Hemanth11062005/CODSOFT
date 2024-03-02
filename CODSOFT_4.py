from tkinter import *
import random

def playgame():
    user_choice = userchoice_var.get()
    computer_choice = random.choice(choices)
    computerchoice_var.set(computer_choice)

    if user_choice == computer_choice:
        resultvar.set("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        resultvar.set("You win!")
        userscore_var.set(userscore_var.get() + 1)
    else:
        resultvar.set("You lose!")
        computerscore_var.set(computerscore_var.get() + 1)

window = Tk()
window.title("Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

userchoice_label = Label(window, text="Your choice:")
userchoice_label.grid(row=0, column=0, padx=5, pady=5)

userchoice_var = StringVar()
userchoice_var.set("rock")

userchoice_menu = OptionMenu(window, userchoice_var, *choices)
userchoice_menu.grid(row=0, column=1, padx=5, pady=5)

computerchoice_label = Label(window, text="Computer's choice:")
computerchoice_label.grid(row=1, column=0, padx=5, pady=5)

computerchoice_var = StringVar()
computerchoice_var.set("")

computerchoice_display = Label(window, textvariable=computerchoice_var)
computerchoice_display.grid(row=1, column=1, padx=5, pady=5)

resultvar = StringVar()
resultlabel = Label(window, textvariable=resultvar)
resultlabel.grid(row=2, columnspan=2, padx=5, pady=5)

userscore_var = IntVar()
userscore_var.set(0)

computerscore_var = IntVar()
computerscore_var.set(0)

scorelabel = Label(window, textvariable=f"Score - You: {userscore_var.get()}, Computer: {computerscore_var.get()}")
scorelabel.grid(row=3, columnspan=2, padx=5, pady=5)

play_button = Button(window, text="Play", command=playgame)
play_button.grid(row=4, columnspan=2, padx=5, pady=5)

window.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from random import randint
from tkinter import font
from tkinter import messagebox  # Import messagebox module for creating popups

# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#F1930C")

# add icon image
photo = PhotoImage(file="rock-paper-scissors.png")
root.iconphoto(False, photo)

# create a font object
label_font = font.Font(weight="bold")

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#F1930C")
comp_label = Label(root, image=scissor_img_comp, bg="#F1930C")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playerScore = Label(root, text=0, font=100, bg="#F1930C", fg="white")
computerScore = Label(root, text=0, font=100, bg="#F1930C", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="#F1930C", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#F1930C", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#F1930C", fg="white")
msg.grid(row=3, column=2)

# update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# Reset scores to 0
def resetScores():
    playerScore["text"] = "0"
    computerScore["text"] = "0"

# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass

    # Show a popup when the match finishes
    if int(playerScore["text"]) == 3 or int(computerScore["text"]) == 3:
        if int(playerScore["text"]) == 3:
            result = "You Win!"
        else:
            result = "Computer Wins!"
        messagebox.showinfo("Game Over", result)
        resetScores()

# update choices
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)

# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

# exit window
def close():
    root.destroy()

# button for closing
exit_button = Button(root, width=15, height=2, text="EXIT", command=close, bg="#FF0000", fg="white").grid(row=0, column=5)

root.mainloop()

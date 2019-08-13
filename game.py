from tkinter import *
from tkinter import messagebox
import ttt

HEIGHT = 200
WIDTH = 150

##TODO:
#Allow player to submit moves in a seperate window
def runGame():
    if roundsEntry.get():
        ttt.AI_select[0] = var1.get()
        ttt.AI_select[1] = var2.get()
        messagebox.showinfo("Game", "X O D\n" + ttt.driver(roundsEntry.get()))

root = Tk()
root.title("Unbeatable Tic Tac Toe")
root.geometry("400x500")

# canvas = Canvas(root, height=HEIGHT, width = WIDTH)

# canvas.pack()

player1L = Label(root, text="Who's X")
player1L.grid(row=0, column=0)
player2L = Label(root, text="Who's O")
player2L.grid(row=0, column=1)

var1 = StringVar(root)
var1.set("choose")
var2 = StringVar(root)
var2.set("choose")

roundsLabel = Label(root, text="How many rounds to play?")
roundsLabel.grid(row=7, column = 0)
roundsEntry = Spinbox(root, from_=0, to=100)
roundsEntry.grid(row=7, column=1)


P1a = Radiobutton(root, text = "Human player", variable = var1, value= "player")
P1b = Radiobutton(root, text = "Random AI", variable = var1, value= "randomAI")
P1c = Radiobutton(root, text = "Winning AI", variable = var1, value= "winningAI")
P1d = Radiobutton(root, text = "Winning & Blocking AI", variable = var1, value= "blockingAI")
P1e = Radiobutton(root, text = "Minimax god", variable = var1, value= "minimaxAI")
P1a.grid(row=1, column=0)
P1b.grid(row=2, column=0)
P1c.grid(row=3, column=0)
P1d.grid(row=4, column=0)
P1e.grid(row=6, column=0)

P1a = Radiobutton(root, text = "Human player", variable = var2, value= "player")
P1b = Radiobutton(root, text = "Random AI", variable = var2, value= "randomAI")
P1c = Radiobutton(root, text = "Winning AI", variable = var2, value= "winningAI")
P1d = Radiobutton(root, text = "Winning & Blocking AI", variable = var2, value= "blockingAI")
P1e = Radiobutton(root, text = "Minimax god", variable = var2, value= "minimaxAI")
P1a.grid(row=1, column=1)
P1b.grid(row=2, column=1)
P1c.grid(row=3, column=1)
P1d.grid(row=4, column=1)
P1e.grid(row=6, column=1)

button = Button(root, text = "run game", command=runGame)
button.grid(row=8, column=1)


root.mainloop()

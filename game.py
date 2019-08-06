from tkinter import *
from tkinter import messagebox
import ttt

HEIGHT = 200
WIDTH = 200

def runGame():
    if roundsEntry.get():
        #TODO: let game.py modify these vars
        ttt.setP1AI(var1)
        ttt.setP2AI(var2)
        messagebox.showinfo("Game", "X O D\n" + ttt.driver(roundsEntry.get()))

root = Tk()
root.title("Unbeatable Tic Tac Toe")
root.geometry("500x500")

# canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)

# canvas.pack()

player1L = Label(root, text="Who's X")
player1L.grid(row=0, column=1)
player2L = Label(root, text="Who's O")
player2L.grid(row=0, column=2)

var1 = StringVar(root)
var1.set("choose")
var2 = StringVar(root)
var2.set("choose")

player1E = OptionMenu(root, var1, "winningAI", "blockingAI", "minimaxAI", "randomAI")
player1E.grid(row=1, column=1)

player2E = OptionMenu(root, var2, "player", "winningAI", "blockingAI", "minimaxAI")
player2E.grid(row=1, column=2)


roundsLabel = Label(root, text="How many rounds to play?")
roundsLabel.grid(row=5, column = 0)
roundsEntry = Entry(root, bd=5)
roundsEntry.grid(row=5, column=1)


button = Button(root, text = "run game", command=runGame)
button.grid(row=6, column=1)


root.mainloop()

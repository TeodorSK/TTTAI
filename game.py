from tkinter import *
from tkinter import messagebox
import ttt

HEIGHT = 200
WIDTH = 150

##TODO:
#Allow player to submit moves in a seperate window
#check for radio button picked before moving on
def runGame():
    if roundsEntry.get():
        ttt.AI_select[0] = var1.get()
        ttt.AI_select[1] = var2.get()

        if(var1.get()=="player"):
            i = inputWindow()
            i.playerPrompt()

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
var2 = StringVar(root)

roundsLabel = Label(root, text="How many rounds to play?")
roundsLabel.grid(row=7, column = 0)
roundsEntry = Spinbox(root, from_=0, to=100)
roundsEntry.grid(row=7, column=1)

#Generating all radio buttons
players = {
    "Human Player": "player",
    "Random AI": "randomAI",
    "Winning AI": "winningAI",
    "Winning & Blocking AI": "blockingAI",
    "Minimax god": "minimaxAI"
}

i = 0
for val, player in enumerate(players):
    i += 1
    Radiobutton(root,
                text = str(player),
                variable = var1,
                value = players[player]).grid(row=i, column=0)

i = 0
for player in players:
    i += 1
    Radiobutton(root,
                text = str(player),
                variable = var2,
                value = players[player]).grid(row=i, column=1)

button = Button(root, text = "run game", command=runGame)
button.grid(row=8, column=1)

class inputWindow:
    def __init__(self):
        self.top = Toplevel()

    def playerPrompt(self):

        self.top.title("Choose your move:")
        self.top.geometry("200x200")
        msg = Message(self.top, text="testy")
        msg.pack()

        submitButton = Button(self.top, text="Submit move", command=self.sendMove)
        submitButton.pack()

    def sendMove(self):
        print("heha")
        self.top.destroy()



root.mainloop()

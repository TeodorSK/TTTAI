from tkinter import *
from tkinter import messagebox
import ttt

HEIGHT = 200
WIDTH = 150

#hehe

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
var1.set("randomAI")
var2 = StringVar(root)
var2.set("randomAI")

roundsLabel = Label(root, text="How many rounds to play?")
roundsLabel.grid(row=7, column = 0)
roundsEntry = Spinbox(root, from_=0, to=100)
roundsEntry.grid(row=7, column=1)

#Generating all radio buttons
players = {
    "Player (test)": "player",
    "Random AI": "randomAI",
    "Winning AI": "winningAI",
    "Winning & Blocking AI": "blockingAI",
    "Minimax god": "minimaxAI"
}

for (index, player) in enumerate(players):
    Radiobutton(root,
                indicatoron = 0,
                text = str(player),
                variable = var1,
                value = players[player]).grid(row=index+2, column=0)

for (index, player) in enumerate(players):
    Radiobutton(root,
                indicatoron = 0,
                text = str(player),
                variable = var2,
                value = players[player]).grid(row=index+2, column=1)

button = Button(root, text = "run game", command=runGame)
button.grid(row=8, column=1)

class inputWindow:

    def __init__(self):
        self.top = Toplevel()

    def playerPrompt(self):

        self.top.title("Choose your move:")
        self.top.geometry("200x200")
        for i in range(0,9):
            row = int(i%3)
            col = int(i/3)

            #Lambda func below uses default values for row, col params, dynamically assigns different functions to each button
            Button(self.top,
                text="[]",
                command=lambda row=row, col=col: self.sendMove(row, col)).grid(row=row, column=col)


        submitButton = Button(self.top, text="Submit move", command=self.sendMove)


    def sendMove(self, row, col):
        print(str(row) + " " + str(col))        
        self.top.destroy()



root.mainloop()

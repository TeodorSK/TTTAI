from tkinter import *
from tkinter import messagebox
import ttt

HEIGHT = 200
WIDTH = 150

def runGame():
    if roundsEntry.get():
        ttt.AI_select[0] = player1.get()
        ttt.AI_select[1] = player2.get()

        if(player1.get()=="player"):
            i = inputWindow()
            i.playerPrompt()

        gameResults = ttt.driver(roundsEntry.get(), showBoardFlag.get())
        #pass showboardFlag
        messagebox.showinfo("Game", "X O D\n" + gameResults)


root = Tk()
root.title("Unbeatable Tic Tac Toe")
root.geometry("400x500")

# canvas = Canvas(root, height=HEIGHT, width = WIDTH)

# canvas.pack()

player1L = Label(root, text="Who's X")
player1L.grid(row=0, column=0)
player2L = Label(root, text="Who's O")
player2L.grid(row=0, column=1)

player1 = StringVar(root)
player1.set("randomAI")
player2 = StringVar(root)
player2.set("randomAI")
showBoardFlag = BooleanVar(root)
showBoardFlag.set(False)


roundsLabel = Label(root, text="How many rounds to play?")
roundsLabel.grid(row=7, column = 0)
roundsEntry = Spinbox(root, from_=0, to=100)
roundsEntry.grid(row=7, column=1)

#Generating all radio buttons
players = {
    "Human": "player",
    "Random AI": "randomAI",
    "Winning AI": "winningAI",
    "Winning & Blocking AI": "blockingAI",
    "Minimax god": "minimaxAI"
}

for (index, player) in enumerate(players):
    Radiobutton(root,
                indicatoron = 0,
                text = str(player),
                variable = player1,
                value = players[player]).grid(row=index+2, column=0)

for (index, player) in enumerate(players):
    Radiobutton(root,
                indicatoron = 0,
                text = str(player),
                variable = player2,
                value = players[player]).grid(row=index+2, column=1)

showBoardCheckbox = Checkbutton(root, text = "Show board after each move?", variable = showBoardFlag)
showBoardCheckbox.grid(row=9, column=1)
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

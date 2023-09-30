from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Камень, ножницы, бумага")

userScore = 0
botScore = 0

def resetScore():
    global userScore, botScore
    userScore = 0
    botScore = 0
    scoreTable.configure(text="Игрок: 0 | Бот: 0")

def clickButton(playerChoose):
    botChoiseArr = ["Камень", "Ножницы", "Бумага"]
    botChoise = random.choice(botChoiseArr)
    global userScore, botScore

    moveLabel.configure(text=f"{playerChoose} | {botChoise}")
    if playerChoose==botChoise:
        whoWinLabel.configure(text="Ничья")
    elif ((playerChoose=="Камень" and botChoise=="Ножницы")
        or (playerChoose=="Бумага" and botChoise=="Камень") or
        (playerChoose=="Ножницы" and botChoise=="Бумага")):
        whoWinLabel.configure(text="Игрок победил!")
        userScore = userScore + 1
    else:
        botScore = botScore + 1
        whoWinLabel.configure(text="Бот победил!")

    scoreTable.configure(text=f"Игрок: {userScore} | Бот: {botScore}")

rockButton = ttk.Button(root, text="Камень", command=lambda: clickButton("Камень"))
scissorsBtn = ttk.Button(root, text="Ножницы", command=lambda: clickButton("Ножницы"))
paperBtn = ttk.Button(root, text="Бумага", command=lambda: clickButton("Бумага"))

whoWinLabel = ttk.Label(root, text="Ничья")
whoMoveLabel = ttk.Label(root, text="Игрок сходил | Бот сходил")
moveLabel = ttk.Label(root, text="Ножницы | Бумага")

scoreTable = ttk.Label(root, text="Игрок: 0 | Бот: 0")
resetBtn = ttk.Button(root, text="Обнулить", command=resetScore)

rockButton.grid(row=0, column=0, pady=4)
scissorsBtn.grid(row=0, column=1)
paperBtn.grid(row=0, column=2)

whoWinLabel.grid(row=1, column=0, columnspan=3, pady=4)
whoMoveLabel.grid(row=2, column=0, columnspan=3, pady=4)
moveLabel.grid(row=3, column=0, columnspan=3, pady=4)
scoreTable.grid(row=4, column=0, columnspan=3, pady=4)
resetBtn.grid(row=5, column=0, columnspan=3, pady=4)

root.mainloop()
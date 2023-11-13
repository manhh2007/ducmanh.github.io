from tkinter import*
from database import*


def window():
    #Start

    game = Tk()

    #Size
    game.geometry(f"{WIDTH}x{HEIGHT}+{P_RIGHT}+{P_DOWN}")

    #Title
    game.title("Manh")

    #Icon
    game.iconbitmap("C:/Users/Admin/Downloads/img.ico")

    #Background
    game['bg']=COLOR

    #Risize
    game.resizable(FALSE,FALSE)

    game.mainloop()
window()
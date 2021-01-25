from tkinter import *
from PIL import ImageTk,Image
import random
root = Tk()
root.geometry("800x700")
img = Image.open("images/DICE.png")
img = img.resize((200, 200), Image.ANTIALIAS)
game_img = ImageTk.PhotoImage(img)
g_label = Label(root, image=game_img)
g_label.grid(row=0, column=0, padx=(300,0))
game_info = Label(root, text=" Hello there, this is dice rolling simulator.\n           "
                             "Press the button to generate new combinations", font=30)
game_info.grid(row=1, column=0)

def dice_simulation():
    #dice 1
    global dice_img_fv_1
    num_1 = str(random.randint(1, 6))
    path_1 = "images/" + num_1 + ".png"
    dice_img_fv_1 = ImageTk.PhotoImage(Image.open(path_1))
    dice_simulator_1 = Label(root, image=dice_img_fv_1)
    dice_simulator_1.grid(row=2, column=0, sticky="W", padx=(50, 0), pady=(50, 50))

    #dice 2
    global dice_img_fv
    num = str(random.randint(1, 6))
    path = "images/" + num + ".png"
    dice_img_fv = ImageTk.PhotoImage(Image.open(path))
    dice_simulator = Label(root, image=dice_img_fv)
    dice_simulator.grid(row=2, column=1, sticky="W", pady=(50, 50))


play_btn = Button(root, text="Press", font=25, command=dice_simulation)
play_btn.place(x=400, y=650)

root.mainloop()

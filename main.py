import random
from tkinter import *
import pandas
from setuptools._distutils.dist import command_re

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash-cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def set_french_word():
    try:
        data = pandas.read_csv("data/french_words.csv")
    except FileNotFoundError:
        pass
    else:
        french_list = data.to_dict(orient="records")
        canvas2.itemconfig(label_title, text="French")
        canvas2.itemconfig(label_word, text=random.choice(french_list)['French'])


canvas1 = Canvas(bg=BACKGROUND_COLOR, width=900, height=650, highlightthickness=0)
image1 = PhotoImage(file="images/card_back.png", width=800, height=530)
canvas1.create_image(450, 280, image=image1)
canvas1.grid(row=0, column=0, columnspan=2)

canvas2 = Canvas(bg=BACKGROUND_COLOR, width=900, height=650, highlightthickness=0)
image2 = PhotoImage(file="images/card_front.png", width=800, height=530)
canvas2.create_image(450, 280, image=image2)
label_title = canvas2.create_text(450, 150, text="", font=("Arial", 40, "italic"))
label_word = canvas2.create_text(450, 300, text="", font=("Arial", 60, "bold"))
canvas2.grid(row=0, column=0, columnspan=2)

image3 = PhotoImage(file="images/wrong.png")
button1 = Button(image=image3, highlightthickness=0, command=set_french_word)
button1.grid(row=1, column=0)

image4 = PhotoImage(file="images/right.png")
button2 = Button(image=image4, highlightthickness=0, command=set_french_word)
button2.grid(row=1, column=1)

set_french_word()

window.mainloop()

import random
import time
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
random_choice = {}
timer = ""

window = Tk()
window.title("Flash-cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def set_french_word():
    global random_choice, timer
    try:
        data = pandas.read_csv("data/french_words.csv")
    except FileNotFoundError:
        pass
    else:
        french_list = data.to_dict(orient="records")
        canvas.itemconfig(bg_img, image=image_front)
        canvas.itemconfig(label_title, text="French", fill="black")
        random_choice = random.choice(french_list)
        canvas.itemconfig(label_word, text=random_choice['French'], fill="black")

    timer = window.after(3000, set_english_word)


def set_english_word():
    global random_choice, timer
    canvas.itemconfig(bg_img, image=image_back)
    canvas.itemconfig(label_title, text="English", fill="white")
    canvas.itemconfig(label_word, text=random_choice['English'], fill="white")
    window.after_cancel(timer)


canvas = Canvas(bg=BACKGROUND_COLOR, width=900, height=560, highlightthickness=0)
image_back = PhotoImage(file="images/card_back.png", width=800, height=530)
image_front = PhotoImage(file="images/card_front.png", width=800, height=530)
bg_img = canvas.create_image(450, 280, image=image_front)
label_title = canvas.create_text(450, 150, text="", font=("Arial", 40, "italic"))
label_word = canvas.create_text(450, 300, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image3 = PhotoImage(file="images/wrong.png")
button1 = Button(image=image3, highlightthickness=0, command=set_french_word)
button1.grid(row=1, column=0)

image4 = PhotoImage(file="images/right.png")
button2 = Button(image=image4, highlightthickness=0, command=set_french_word)
button2.grid(row=1, column=1)

set_french_word()

window.mainloop()

import random
import time
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
random_choice = {}
timer = ""
word_list = {}

window = Tk()
window.title("Flash-cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def set_french_word():
    global random_choice, timer, word_list
    try:
        data = pandas.read_csv("data/to_learn.csv")
    except FileNotFoundError:
        og_data = pandas.read_csv("data/french_words.csv")
        word_list = og_data.to_dict(orient="records")
    else:
        word_list = data.to_dict(orient="records")
        canvas.itemconfig(bg_img, image=image_front)
        canvas.itemconfig(label_title, text="French", fill="black")
        random_choice = random.choice(word_list)
        canvas.itemconfig(label_word, text=random_choice['French'], fill="black")

    timer = window.after(3000, set_english_word)


def set_english_word():
    global random_choice, timer
    canvas.itemconfig(bg_img, image=image_back)
    canvas.itemconfig(label_title, text="English", fill="white")
    canvas.itemconfig(label_word, text=random_choice['English'], fill="white")
    window.after_cancel(timer)


def correct_word():
    global word_list, random_choice
    word_list.remove(random_choice)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/to_learn.csv", index=False)
    set_french_word()


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
button2 = Button(image=image4, highlightthickness=0, command=correct_word)
button2.grid(row=1, column=1)

set_french_word()

window.mainloop()

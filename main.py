from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash-cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas1 = Canvas(bg=BACKGROUND_COLOR, width=900, height=650, highlightthickness=0)
image1 = PhotoImage(file="images/card_back.png", width=800, height=530)
canvas1.create_image(450, 280, image=image1)
canvas1.grid(row=0, column=0, columnspan=2)

canvas2 = Canvas(bg=BACKGROUND_COLOR, width=900, height=650, highlightthickness=0)
image2 = PhotoImage(file="images/card_front.png", width=800, height=530)
canvas2.create_image(450, 280, image=image2)
canvas2.grid(row=0, column=0, columnspan=2)

image3 = PhotoImage(file="images/wrong.png")
button1 = Button(image=image3, highlightthickness=0)
button1.grid(row=1, column=0)

image4 = PhotoImage(file="images/right.png")
button2 = Button(image=image4, highlightthickness=0)
button2.grid(row=1, column=1)

window.mainloop()

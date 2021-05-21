from tkinter import *
import pandas
import random

card1_text1 = None
card1_text2 = None
right_img = None
word_card = {}

data_file = pandas.read_csv("data/french_words.csv")
data = data_file.to_dict(orient="records")
print(data)
# dict = {k:v for (k, v) in zip(data["French"], data['English'])}

def next_word():
    global word_card, flip_timer
    window.after_cancel(flip_timer)
    word_card = random.choice(data)
    canvas.itemconfig(card1_text1, text=f"French", fill="black")
    canvas.itemconfig(card1_text2, text=f"{word_card['French']}", fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global word_card
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(card1_text1, text=f"English", fill="White")
    canvas.itemconfig(card1_text2, text=f"{word_card['English']}", fill="White")




BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy Translate Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=500, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image(400, 250, image=card_front)
card1_text1 = canvas.create_text(400, 130, text="", fill="black", font=("Arial", 40, "italic"))
card1_text2 = canvas.create_text(400, 330, text="", fill="black", font=("Arial", 70, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

card_back = PhotoImage(file="images/card_back.png")

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

button1 = Button(image=wrong_img, highlightthickness=0, command=next_word)
# button1.config(bg=BACKGROUND_COLOR)
button1.grid(column=0, row=1)

button1 = Button(image=right_img, highlightthickness=0, command=next_word)
button1.grid(column=1, row=1)








next_word()



window.mainloop()


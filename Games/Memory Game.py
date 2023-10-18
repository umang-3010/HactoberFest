import random
from tkinter import *
from tkinter import messagebox

# Defining the display window
root = Tk()
root.title("Meomory Game")
root.geometry("500x500")

# Some variables
global winner, cards
winner = 0
count = 0
answer_list = []
answer_dict = {}

# Creating and shuffling the cards
cards = [1, 2, 3, 4, 5, 6] * 2
random.shuffle(cards)

# Creating Frame for button
frame = Frame(root)
frame.pack(pady=10)


def win():
    my_label.config(text="Congratulations! You Won!!!")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # Loop through buttons and change colors
    for button in button_list:
        button.config(bg="yellow")


def button_click(button, button_index):
    global count, answer_list, answer_dict, winner

    if button["text"] == ' ' and count < 2:
        button["text"] = cards[button_index]
        # Add number to answer list
        answer_list.append(button_index)
        # Add button and number to Answer Dictionary
        answer_dict[button] = cards[button_index]
        # Increment our Counter
        count += 1
    # print(answer_dict)

    # Start to determine correct or not
    if len(answer_list) == 2:
        if cards[answer_list[0]] == cards[answer_list[1]]:
            my_label.config(text="MATCH!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
            # Increment our winner counter
            winner += 1
            if winner == 6:
                win()
        else:
            # my_label.config(text="DOH!")
            count = 0
            answer_list = []
            # pop up box
            messagebox.showinfo("Incorrect!", "Incorrect")

            # Reset the buttons
            for key in answer_dict:
                key["text"] = " "

            answer_dict = {}


def reset():
    global cards, winner
    winner = 0
    cards = [1, 2, 3, 4, 5, 6] * 2
    random.shuffle(cards)

    # Reset Label
    my_label.config(text="")

    # Reset our Tiles
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # Loop through buttons and change colors
    for button in button_list:
        button.config(text=" ", bg="SystemButtonFace", state="normal")


# Creating button for each card
b0 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b0, 0),
            relief="groove")
b1 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b1, 1),
            relief="groove")
b2 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b2, 2),
            relief="groove")
b3 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b3, 3),
            relief="groove")
b4 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b4, 4),
            relief="groove")
b5 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b5, 5),
            relief="groove")
b6 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b6, 6),
            relief="groove")
b7 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b7, 7),
            relief="groove")
b8 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b8, 8),
            relief="groove")
b9 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b9, 9),
            relief="groove")
b10 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b10, 10),
             relief="groove")
b11 = Button(frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b11, 11),
             relief="groove")

# Grid our Buttons
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)

# Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create an Options Dropdown Menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game", command=root.quit)

root.mainloop()
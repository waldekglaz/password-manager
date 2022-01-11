from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t","u","v",
        "w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U",
        "V","W","X", "Y", "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ------------------------ SAVE PASSWORD -------------------------- #


def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()
    if len(password) < 2 or len(website) < 2:
        messagebox.showinfo(title="Error", message="Fields cannot be empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {user}\nPassword: {password}\nIs it ok to save?",
        )
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {user} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ------------------------ UI SETUP -------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(heigh=200, width=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)
# ---------- Labels
website_url_label = Label(text="Website:")
website_url_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# ------ Entries
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
user_input = Entry(width=35)
user_input.insert(0, "waldekglaz@gmail.com")
user_input.grid(column=1, row=2, columnspan=2, sticky="EW")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="W")
# ------ Buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")
add_btn = Button(width=36, text="Add", command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
window.mainloop()

from tkinter import *

# ------------------------ SAVE PASSWORD -------------------------- #
def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {user} | {password}\n")

# ------------------------ UI SETUP -------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(heigh=200, width = 200)
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
generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3, sticky="EW")
add_btn = Button(width=36, text="Add", command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
window.mainloop()
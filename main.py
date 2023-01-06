from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
bg_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_photo)
canvas.grid(column=1, row=0)

lbl_website = Label(text="Website:")
lbl_website.grid(column=0, row=1)

lbl_username = Label(text="Email/Username:")
lbl_username.grid(column=0, row=2)

lbl_password = Label(text="Password:")
lbl_password.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)

entry_username = Entry(width=35)
entry_username.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=35)
entry_password.grid(column=1, row=3, columnspan=2)

btn_generate_pass = Button(text="Generate Password", width=30)
btn_generate_pass.grid(column=1, row=4, columnspan=2)

btn_add = Button(text="Add", width=25)
btn_add.grid(column=1, row=5, columnspan=2)

window.mainloop()

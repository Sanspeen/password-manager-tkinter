from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    entry_password.delete(0, END)
    entry_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if website != "" and username != "" and password != "":
        confirmation_to_save = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                                             f"\n-> Email: {username} \n-> Password:"
                                                                             f" {password}\nIs it ok to save?")
        if confirmation_to_save:
            new_data = {
                website:{
                    "email": username,
                    "password": password
                }
            }
            with open("data.json", "r") as passwords:
                # Reading old data
                data = json.load(passwords)

                # Updating old data
                data.update(new_data)

            with open("data.json", "w") as passwords:
                # Saving updated data
                json.dump(data, passwords, indent=4)

            entry_website.delete(0, END)
            entry_username.delete(0, END)
            entry_password.delete(0, END)

            messagebox.showinfo(title="Congratulations!", message="Your password info has been saved")

        else:
            messagebox.showinfo(title="Cancelled", message="You has discarded this info :'D")

    else:
        messagebox.showinfo(title="Oops", message="Please don't let any field empty!")


# ---------------------------- UI SETUP ------------------------------- #
main_window = Tk()
main_window.title("Password Manager")
main_window.config(padx=20, pady=20)

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
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2)

entry_username = Entry(width=35)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "example@gmail.com")

entry_password = Entry(width=35)
entry_password.grid(column=1, row=3, columnspan=2)

btn_generate_pass = Button(text="Generate Password", width=30, command=password_generator)
btn_generate_pass.grid(column=1, row=4, columnspan=2)

btn_add = Button(text="Add", width=25, command=save_password)
btn_add.grid(column=1, row=5, columnspan=2)

main_window.mainloop()


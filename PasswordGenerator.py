import random
import tkinter as tk


def generate_password():
    all_chars = ""
    if caps_var.get():
        all_chars += uppercase_letters
    if lows_var.get():
        all_chars += lowercase_letters
    if nums_var.get():
        all_chars += digits
    if symb_var.get():
        all_chars += symbols

    length = int(length_entry.get())
    password = ''.join(random.sample(all_chars, length))
    password_display.config(text=password)


uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "()[]{},;:._-!@#$%^&*/\\?+="

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")

caps_var = tk.BooleanVar(value=True)
lows_var = tk.BooleanVar(value=True)
nums_var = tk.BooleanVar(value=True)
symb_var = tk.BooleanVar(value=True)

tk.Label(root, text="PASSWORD GENERATOR", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Enter your desired length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

tk.Checkbutton(root, text="Include uppercase letters", variable=caps_var).pack(anchor="w")
tk.Checkbutton(root, text="Include lowercase letters", variable=lows_var).pack(anchor="w")
tk.Checkbutton(root, text="Include numbers", variable=nums_var).pack(anchor="w")
tk.Checkbutton(root, text="Include symbols", variable=symb_var).pack(anchor="w")

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=10)

password_display = tk.Label(root, text="")
password_display.pack()

root.mainloop()

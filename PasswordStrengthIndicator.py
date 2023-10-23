
import tkinter as tk

def calculate_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(not char.isalnum() for char in password)

    strength = 0

    if length >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special_char:
        strength += 1

    return strength

def update_strength():
    password = password_entry.get()
    strength = calculate_password_strength(password)

    if strength < 3:
        strength_label.config(text="Password Strength: Weak")
    elif strength < 4:
        strength_label.config(text="Password Strength: Medium")
    else:
        strength_label.config(text="Password Strength: Strong")

# Create the main window
root = tk.Tk()
root.title("Password Strength Indicator")

# Create and configure the password entry
password_label = tk.Label(root, text="Enter Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
password_entry.bind("<KeyRelease>", lambda event: update_strength())

# Create and configure the strength label
strength_label = tk.Label(root, text="Password Strength: Weak")
strength_label.pack()

root.mainloop()



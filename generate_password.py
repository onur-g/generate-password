import tkinter as tk

window = tk.Tk()

# Window size
window.geometry("800x800")

# Frame
frame = tk.Frame(window, relief="ridge", bg="#ADD8E6")
frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

# Greeting
greeting = tk.Label(frame, text="  Welcome to Onur's Password Manager  ", fg="white", font="Times 24", bg="#00008B")
greeting.pack(pady=70)

# Length textbox
length_label = tk.Label(frame, text="Length", fg="white", bg="black")
length_label.pack(pady=10)
length_box = tk.Text(frame, height=1, width=10, padx=5, pady=5)
length_box.pack()

# Mode radiobuttons
modes_label = tk.Label(frame, text="Mode", fg="white", bg="black")
modes_label.pack(pady=10)
modes = ["Easy to say", "Easy to read", "All characters"]
var = tk.IntVar()
var.set(0)

for i, mode in enumerate(modes):
    mode_button = tk.Radiobutton(frame, text=mode, variable=var, value=i)
    mode_button.pack()

# Set preferences based on input
len = 12
mode = 2
upper = True
lower = True
numbers = True
symbols = True

# Create string of possible characters based on preferences
possible = ""
if upper:
    possible += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if lower:
    possible += "abcdefghijklmnopqrstuvwxyz"
if numbers:
    possible += "0123456789"
if symbols:
    possible += "!@#$%^&*()_+,.[];"

# Generate random password
password = ""
import random
for i in range(len):
    password += random.choice(possible)

# Copy generated password to clipboard
import subprocess
subprocess.run("clip", text=True, input=password)

print(password)

window.mainloop()
import tkinter as tk

window = tk.Tk()

window.geometry("800x800")

frame = tk.Frame(window, relief="ridge", bg="#ADD8E6")
frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

greeting = tk.Label(frame, text="  Welcome to Onur's Password Manager  ", fg="white", font="Times 24", bg="#00008B")
greeting.pack(pady=70)

len = 12
mode = 2
upper = True
lower = True
numbers = True
symbols = True

possible = ""

if upper:
    possible += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if lower:
    possible += "abcdefghijklmnopqrstuvwxyz"
if numbers:
    possible += "0123456789"
if symbols:
    possible += "!@#$%^&*()_+,.[];"

password = ""

import random
for i in range(len):
    password += random.choice(possible)

import subprocess
subprocess.run("clip", text=True, input=password)

print(password)

window.mainloop()
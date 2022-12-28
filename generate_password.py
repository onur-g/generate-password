import random

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

for i in range(len):
    password += random.choice(possible)

print(password)
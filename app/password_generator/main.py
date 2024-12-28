import random
import string

pass_len = input("enter the length of the password=",)
pass_len = int(pass_len)

count = 0
passw1 = []

while True:
    count = count + 1
    if count > pass_len:
        break
    small_alfa = random.choice(string.ascii_lowercase)
    caps_alfa = random.choice(string.ascii_uppercase)
    numeric = random.choice(string.digits)
    spl_char = random.choice(string.punctuation)
    var = (small_alfa, caps_alfa, numeric, spl_char)
    var01 = random.choice(var)

    passw1.append(var01)
psswd = ''.join(passw1)
print(psswd)
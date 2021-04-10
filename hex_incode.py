import os

os.system("set demo=%demo%>.unicode_hex")

not_first_time = False

while True:
    f = open(".\\.unicode_hex", "a")
    if not_first_time:
        f.write(" " + str(hex(ord("\n")))[2:])
    text = input()
    for i in text:

        if not_first_time:
            f.write(" ")
        f.write(str(hex(ord(i)))[2:])
        not_first_time = True
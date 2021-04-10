text = open(".\\.unicode_hex", "r").read()
new_text = str()
for i in text.split(" "):
    new_text += chr(int(i, 16))
print(new_text)
while True:
    pass
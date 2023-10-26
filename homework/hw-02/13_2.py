message = input("Enter a message: ")
offset = int(input("Enter the offset: "))

encoded_message = ""

for ch in message:
    if ch.isalpha():
        base = ord('a') if ch.islower() else ord('A')

        pos = (ord(ch) - base + offset) % 26 + base

        ch = chr(pos)

    encoded_message += ch

print(f"ciphered text is: '{encoded_message}'")
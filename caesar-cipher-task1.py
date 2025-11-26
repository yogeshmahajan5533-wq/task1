shift=3
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
#            base = ord('A') if char.isupper() else ord('a')
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


# ---- input ----
while True:
    print("\n===== CAESAR CIPHER MENU =====")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            text = input("Enter text to encrypt: ")
            print("Encrypted:", encrypt(text, shift))

        case "2":
            text = input("Enter text to decrypt: ")
            print("Decrypted:", decrypt(text, shift))

        case "3":
            print("Exiting...")
            break

        case _:
            print("Invalid option! Please try again.")
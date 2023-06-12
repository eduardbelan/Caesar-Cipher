from art import logo

print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

alphabet_expanded = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
    '4', '5', '6', '7', '8', '9', '!', '?', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'",
    '"', ',', '.', '/', '<', '>', '~'
]

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = [
    '!', '?', '@', '#', '$', '%', '^', '&', '*', '(',
    ')', '-', '_', '+', '=', '[', ']', '{', '}', '|',
    '\\', ';', ':', "'", '"', ',', '.', '/', '<', '>',
    '~'
]


def caesar(start_text, shift_amount, cipher_direction):
    """
    Determine the cipher message:
    Default: extended alpha
    Change alpha to "alphabet" for caesar_cipher_normal_alpha()
    """
    alpha = alphabet_expanded
    enc = "encode"
    dec = "decode"
    end_text = ""
    if cipher_direction == "d":
        shift_amount *= -1
    for char in start_text:
        if char in alpha:
            position = "".join([alpha[(alpha.index(char) + shift_amount) % 67]])
            end_text += position
        else:
            end_text += char

    if cipher_direction == "e":
        print(f"The {enc}d text is: {end_text}")
    else:
        print(f"The {dec}d text is: {end_text}")


def caesar_cipher_extended_alpha():
    """
    "Extended Alphabet" Version
    """
    while True:
        direction = input("Type 'e' to encrypt, or 'd' to decrypt:\n")

        if direction not in ["e", "d"]:
            print("Invalid input. Please enter 'e' or 'd'.")
            continue

        text = input("Type your message:\n").lower()
        while any(char not in alphabet_expanded for char in text):
            print("Message contains invalid characters.\n"
                  "Valid characters:\n"
                  f"{letters}\n"
                  f"{numbers}\n"
                  f"{symbols}")
            text = input("Type your message:\n").lower()

        while True:
            try:
                shift = int(input("Type the shift number:\n"))
                break
            except ValueError:
                print("Please enter numbers only.")

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        while True:
            restart = input("Type 'y' if you want to go again. Otherwise type 'n'.\n")
            if restart in ["y", "n"]:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if restart == "n":
            print("Goodbye")
            break


caesar_cipher_extended_alpha()


# def caesar_cipher_normal_alpha():
#     """
#     "Normal Alphabet" Version
#     """
#     while True:
#         direction = input("Type 'e' to encrypt, or 'd' to decrypt:\n")
#
#         if direction not in ["e", "d"]:
#             print("Invalid input. Please enter 'e' or 'd'.")
#             continue
#
#         while True:
#             text = input("Type your message:\n").lower()
#             if text.isalpha():
#                 break
#             else:
#                 print("Please enter letters only.")
#
#         while True:
#             try:
#                 shift = int(input("Type the shift number:\n"))
#                 break
#             except ValueError:
#                 print("Please enter numbers only.")
#
#         caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#
#         while True:
#             restart = input("Type 'y' if you want to go again. Otherwise, type 'n'.\n")
#             if restart in ["y", "n"]:
#                 break
#             else:
#                 print("Invalid input. Please enter 'y' or 'n'.")
#
#         if restart == "n":
#             print("Goodbye")
#             break
#
#
# caesar_cipher_normal_alpha()

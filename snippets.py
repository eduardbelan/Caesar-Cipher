from art import logo

print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# old version
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode" or direction == "decode":
        # only letters pass
        is_txt = False
        while not is_txt:
            text = input("Type your message:\n").lower()
            if text.isalpha():
                is_txt = True
                break
            else:
                print("Please enter letters only.")
        # only numbers pass
        is_int = False
        while not is_int:
            try:
                shift = int(input("Type the shift number:\n"))
                is_int = True
            except ValueError:
                print("Please enter numbers only.")

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        # restart should be y or n
        restart = input(
            "Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
        if restart == "no":
            should_end = True
            print("Goodbye")

    else:
        correct = False
        while not correct:

            direction = input("Type 'encode' or type 'decode':\n")

            if direction == "encode" or direction == "decode":
                correct = True

                # only letters pass
                is_txt = False
                while not is_txt:
                    text = input("Type your message:\n").lower()
                    if text.isalpha():
                        is_txt = True
                        break
                    else:
                        print("Please enter letters only.")

                # only numbers pass
                is_int = False
                while not is_int:
                    try:
                        shift = int(input("Type the shift number:\n"))
                        is_int = True
                    except ValueError:
                        print("Please enter numbers only.")

                caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
                restart = input(
                    "Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
                if restart == "no":
                    should_end = True
                    print("Goodbye")
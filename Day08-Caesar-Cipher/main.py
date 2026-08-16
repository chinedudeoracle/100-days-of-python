alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = ".... .. .. 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
            
    print(f"Here is the {cipher_direction}d result: {end_text}")

from art import logo

print(logo)

continue_cipher = True

while continue_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decript:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26 

    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if response == "no":
        continue_cipher = False
        print("Goodbye")
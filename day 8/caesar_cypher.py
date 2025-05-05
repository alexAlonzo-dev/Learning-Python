# Banner ASCII personalizado
print(r"""
                     --- alex's encrypt ---
""")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_decode):
    output_text = ""

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if encode_decode == "decode":
                shift_letter = alphabet[(position - shift_amount) % 26]
            else:
                shift_letter = alphabet[(position + shift_amount) % 26]
            output_text += shift_letter
        else:
            output_text += letter  

    print(f"\nHere is the {encode_decode}d output: {output_text}\n")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(text, shift, direction)

    again = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    if again != 'yes':
        should_continue = False
        print("Goodbye!")

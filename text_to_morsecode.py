

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}
flag = True
print("Welcome to the Morse code converter!")

while(True):
    sentence = input("Enter a sentence to convert to Morse code: ")
    for i in sentence:
        if i.upper() in morse_code_dict:
            print(morse_code_dict[i.upper()], end=' ')
        else:
            print('', end=' ')

    print()  # For a new line after the Morse code output
    print("Conversion to Morse code completed.")

    user_input = input("Do you want to convert another sentence? (yes/no): ").strip().lower()
    if user_input == 'yes':
        continue
    else:
        break

print("Thank you for using the Morse code converter!")
print("Goodbye!")
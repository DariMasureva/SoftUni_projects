engl_to_morse = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

morse_to_engl = {value: key for key, value in engl_to_morse.items()}

deciphered_message = ''
words = input().split(" | ")

for word in words:
    morse_letters = word.split()

    for morse_letter in morse_letters:
        engl_letter = morse_to_engl[morse_letter]
        deciphered_message += engl_letter

    deciphered_message += ' '

print(deciphered_message)

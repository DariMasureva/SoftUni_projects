alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

c_counter = 0
o_counter = 0
n_counter = 0
current_word = ''
whole_str = ""

command = input()

while command != "End":
    if command in alphabet:
        if command == "c" and c_counter == 0:
            c_counter += 1
        elif command == "o" and o_counter == 0:
            o_counter += 1
        elif command == "n" and n_counter == 0:
            n_counter += 1
        else:
            current_word += command

        if c_counter == 1 and o_counter == 1 and n_counter == 1:
            current_word += " "
            c_counter = 0
            o_counter = 0
            n_counter = 0
            whole_str += current_word
            current_word = ""

        command = input()

    else:
        command = input()
        continue

print(whole_str)

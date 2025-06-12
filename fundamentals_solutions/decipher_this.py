initial_message = input().split()
new_message = []

for word in initial_message:
    first_letter = "".join(filter(lambda x: x.isdigit(), word))
    letters = [letter for letter in word if letter.isalpha()]

    if len(letters) > 1:
        letters[0], letters[-1] = letters[-1], letters[0]

    first_letter = chr(int(first_letter))
    letters.insert(0, first_letter)
    new_message.append("".join(letters))

print(" ".join(new_message))

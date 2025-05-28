# 🧵 Python Text Transformation Toolkit

# Step 1: Display a menu to the user
print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get the input string
text = input("Enter the text: ")

# Step 4: Apply the selected transformation
if choice == 1:

    initial_text_list = list(text)
    reversed_text = []

    for char in reversed(text):
        reversed_text.append(char)

    print("".join(reversed_text))

elif choice == 2:

    text.upper()
    print(text)

elif choice == 3:

    text.lower()
    print(text)

elif choice == 4:

    text.split()
    initial_text_list = list(text)
    capitalized_text_list = []

    for word in initial_text_list:
        word.capitalize()
        capitalized_text_list.append(word)

    " ".join(capitalized_text_list)

    print(capitalized_text_list)

elif choice == 5:

    vowel_str = "aeiou"
    text.lower()
    vowels_found = 0

    for char in text:
        if char in vowel_str:
            vowels_found += 1

    print(vowels_found)

elif choice == 6:

    text.replace(" ", "")

    print(text)

elif choice == 7:

    vowel_str = "aeiou"
    initial_text_list = list(text.lower())
    replaced_vowels_list = ["*" if char in vowel_str else char for char in initial_text_list]

    print("".join(replaced_vowels_list))

elif choice == 8:

    initial_text_list = list(text.lower())
    formatted = "".join([char for char in initial_text_list if char != " "])
    is_palindrome = False

    if formatted == formatted[::-1]:
        is_palindrome = True

    if is_palindrome:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")

elif choice == 9:

    text.split()
    counter_list = []

    while text:
        curr_word = text[0]
        curr_counter = text.count(curr_word)

        counter_list.append((curr_word, curr_counter))
        text = [word for word in text if word != curr_word]

    print(counter_list)

else:
    print("❌ Invalid choice! Please restart the program.")

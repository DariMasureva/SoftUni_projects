def chars_in_range(first_char, last_char):
    first_ascii = ord(first_char)
    last_ascii = ord(last_char)
    result_string = ""

    for cur_char in range(first_ascii + 1, last_ascii):
        cur_char = chr(cur_char)

        if ord(cur_char) != last_ascii - 1:
            cur_char += " "

        result_string += cur_char

    return result_string


start_char = input()
stop_char = input()

print(chars_in_range(start_char, stop_char))

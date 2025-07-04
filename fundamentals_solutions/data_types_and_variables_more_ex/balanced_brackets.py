lines_count = int(input())

balanced = True
expected_opening = True
expected_closing = False

for _ in range(lines_count):

    string = input()

    if string == "(" and expected_opening:
        expected_closing = True
        expected_opening = False
    elif string == ")" and expected_closing:
        expected_closing = False
        expected_opening = True
    elif (string == "(" and expected_closing) or (string == ")" and expected_opening):
        balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")

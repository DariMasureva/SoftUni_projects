def multiplication_sign(num1, num2, num3):
    negatives_count = 0
    number_list = [num1, num2, num3]

    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"

    for number in number_list:
        if number < 0:
            negatives_count += 1

    if negatives_count % 2 == 0:
        return "positive"
    else:
        return "negative"


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(multiplication_sign(number1, number2, number3))

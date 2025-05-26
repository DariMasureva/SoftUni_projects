num1 = int(input())
num2 = int(input())
operator = input()

result = 0
even_odd = "odd"

if operator in ["+", "-", "*"]:
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2

    remainder = result % 2
    if remainder == 0:
        even_odd = "even"
    print(f"{num1} {operator} {num2} = {result} - {even_odd}")

elif operator in ["/", "%"] and num2 != 0:
    if operator == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
    elif operator == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
else:
    print(f"Cannot divide {num1} by zero")

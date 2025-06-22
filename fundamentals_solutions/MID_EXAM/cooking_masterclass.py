from math import ceil

budget = float(input())
student_count = int(input())
flour_single_price = float(input())
egg_single_price = float(input())
apron_single_price = float(input())
total_cost = 0

for student_num in range(1, student_count + 1):
    if student_num % 5 != 0:
        total_cost += flour_single_price

total_cost += egg_single_price * student_count * 10
total_cost += apron_single_price * ceil(student_count * 1.2)

if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{total_cost - budget:.2f}$ more needed.")

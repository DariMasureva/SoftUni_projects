import re

valid_food_pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
all_food = input()
valid_foods = re.findall(valid_food_pattern, all_food)
total_calories = sum(int(food[3]) for food in valid_foods)
total_days = total_calories // 2000

print(f"You have food to last you for: {total_days} days!")

for food in valid_foods:
    name, date, calories = food[1:]
    print(f"Item: {name}, Best before: {date}, Nutrition: {calories}")

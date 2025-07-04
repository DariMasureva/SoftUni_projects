happiness_list = list(map(int, input().split()))
factor = int(input())
happiness_list = [happy_num * factor for happy_num in happiness_list]
total_count = len(happiness_list)
average = sum(happiness_list) / total_count
happy_count = len([happy_num for happy_num in happiness_list if happy_num >= average ])

if happy_count * 2 >= total_count:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")

def perfect_num_check(number_checked: int):
    proper_divisors = [divisor for divisor in range(1, number_checked) if number_checked % divisor == 0]
    sum_of_divisors = sum(proper_divisors)

    if sum_of_divisors == number_checked:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number_given = int(input())
print(perfect_num_check(number_given))

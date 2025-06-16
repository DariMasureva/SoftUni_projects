population_list = list(map(int, input().split(", ")))
min_wealth_goal = int(input())

if sum(population_list) >= min_wealth_goal * len(population_list):

    while min(population_list) < min_wealth_goal:
        min_idx = population_list.index(min(population_list))
        max_idx = population_list.index(max(population_list))
        left_to_min = min_wealth_goal - min(population_list)

        min_wealth = population_list.pop(min_idx)
        min_wealth += left_to_min
        population_list.insert(min_idx, min_wealth)

        max_wealth = population_list.pop(max_idx)
        max_wealth -= left_to_min
        population_list.insert(max_idx, max_wealth)

    print(population_list)

else:
    print("No equal distribution possible")

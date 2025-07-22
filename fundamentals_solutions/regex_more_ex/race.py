import re

racers = {racer: 0 for racer in input().split(", ")}
awards = ["1st", "2nd", "3rd"]
racer_name_pattern = r"[A-Za-z]+"
racer_result_pattern = r"\d"

while (result := input()) != "end of race":
    cur_racer = "".join(re.findall(racer_name_pattern, result))
    # turning all strings to ints and then finding their sum
    cur_result = sum(list(map(int, re.findall(racer_result_pattern, result))))

    if cur_racer in racers:
        racers[cur_racer] += cur_result

for cur_award in awards:
    best_racer = max(racers.keys(), key=lambda racer: racers[racer])
    print(cur_award + f" place: {best_racer}")
    del racers[best_racer]

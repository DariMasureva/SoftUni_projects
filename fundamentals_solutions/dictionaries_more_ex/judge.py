contests = {}
individual_stats = {}

while (submission:=input()) != "no more time":
    username, contest, points = submission.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}

    if username in contests[contest] and points < contests[contest][username]:
        pass
    else:
        contests[contest][username] = points

for contest, results in contests.items():
    print(f"{contest}: {len(results)} participants")

    #sorting by tie-breaker
    results = dict(sorted(results.items(), key=lambda item: item[0]))
    #sortinng by main criterion
    results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

    for idx, (username, points) in enumerate(results.items(), start=1):
        print(f"{idx}. {username} <::> {points}")

# building individual stats by iterating through the existing dict and summing
for contest, results in contests.items():
    for username, points in results.items():
        if username not in individual_stats:
            individual_stats[username] = 0

        individual_stats[username] += points

# sorting by tie-breaker
individual_stats = dict(sorted(individual_stats.items(), key=lambda item: item[0]))
# sorting by main criterion
individual_stats = dict(sorted(individual_stats.items(), key=lambda item: item[1], reverse=True))

print("Individual standings:")
for idx, (username, points) in enumerate(individual_stats.items(), start=1):
    print(f"{idx}. {username} -> {points}")

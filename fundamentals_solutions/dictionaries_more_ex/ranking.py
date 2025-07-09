contest_passwords = {}
contest_results = {}
best_result = 0
best_username = ""

while (info:=input()) != "end of contests":
    contest, password = info.split(":")
    contest_passwords[contest] = password

while (info:=input()) != "end of submissions":
    contest, password, username, points = info.split("=>")
    points = int(points)

    if contest in contest_passwords and password == contest_passwords[contest]:

        if username not in contest_results:
            contest_results[username] = {}

        if contest in contest_results[username] and contest_results[username][contest] >= points:
            pass
        else:
            contest_results[username][contest] = points

contest_results = dict(sorted(contest_results.items()))

for username, personal_results in contest_results.items():
    cur_sum = sum(personal_results.values())
    if cur_sum > best_result:
        best_result = cur_sum
        best_username = username

print(f"Best candidate is {best_username} with total {best_result} points.")
print("Ranking:")

for username, personal_results in contest_results.items():
    personal_results = dict(sorted(personal_results.items(), key=lambda x: x[1], reverse=True))
    print(username)

    for contest, points in personal_results.items():
        print(f"#  {contest} -> {points}")

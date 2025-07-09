exam_results = {}

while (submission := input()) != "exam finished":

    if "banned" in submission:
        name = submission.split("-")[0]
        for language_results in exam_results.values():
            if name in language_results:
                language_results[name].append("banned")

    else:
        name, language, points = submission.split("-")
        points = int(points)

        if language in exam_results:
            if name not in exam_results[language]:
                exam_results[language][name] = [points]
            elif name in exam_results[language]:
                exam_results[language][name].append(points)

        else:
            exam_results[language] = {name: [points]}

print("Results:")
for language, language_results in exam_results.items():
    for name, points in language_results.items():
        if "banned" not in points:
            print(f"{name} | {max(points)}")

print("Submissions:")
for language, language_results in exam_results.items():
    total_submissions = 0
    for points in language_results.values():
        total_submissions += sum([1 for result in points if result != "banned"])
    print(f"{language} - {total_submissions}")

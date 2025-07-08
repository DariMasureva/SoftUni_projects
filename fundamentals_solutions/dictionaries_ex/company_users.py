companies = {}

while (command:=input()) != "End":
    company, empl_id = command.split(" -> ")

    if company in companies:
        if empl_id in companies[company]:
            continue
        else:
            companies[company].append(empl_id)
    else:
        companies[company] = [empl_id]

for company, empl_list in companies.items():
    print(company)
    for empl_id in empl_list:
        print(f"-- {empl_id}")

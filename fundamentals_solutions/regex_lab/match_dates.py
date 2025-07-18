import re
dates = input()
regex = r"\b(\d{2})([.\/-])([A-Z][a-z]{2})\2(\d{4}\b)"
valid_dates = re.finditer(regex, dates)

for date in valid_dates:
        day = date.group(1)
        month = date.group(3)
        year = date.group(4)

        print(f"Day: {day}, Month: {month}, Year: {year}")

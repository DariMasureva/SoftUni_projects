import re

text = input()
pattern = r"\s([a-z0-9][a-z0-9\.\-\_]*@[a-z\-]+(\.[a-z]+)+)\b"
valid_emails = []
emails_found = re.findall(pattern, text)

for email in emails_found:
    valid_emails.append(email[0])
print("\n".join(valid_emails))

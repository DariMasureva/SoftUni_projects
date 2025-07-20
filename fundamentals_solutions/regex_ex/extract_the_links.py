import re

valid_links = []
pattern = r"(www\.[a-zA-Z0-9-]+(\.[a-z]+)+)"

while sentence := input():
    valid_links.extend(link[0] for link in re.findall(pattern, sentence))

print("\n".join(valid_links))

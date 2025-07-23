import re

html = input()
title_pattern = r"<title>(.*)</title>"
whole_body_pattern = r"<body>(.*)</body>"
tags_pattern = r"<[^>]*>"
space_pattern = r"\n|\t|\\n|\\t"

title = re.search(title_pattern, html).group(1)
body = re.search(whole_body_pattern, html).group(1)

title = re.sub(tags_pattern, "", title)
body = re.sub(tags_pattern, "", body)

title = re.sub(space_pattern, "", title)
body = re.sub(space_pattern, "", body)

print("Title:", title)
print("Content:", body)

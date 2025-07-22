import re

html = input()
title_pattern = r"<title>(.*)</title>"
whole_body_pattern = r"<body>(.*)</body>"
body_content_pattern = r""
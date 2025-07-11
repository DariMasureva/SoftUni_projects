title = input()
print(f"<h1>\n{title}\n</h1>")
content = input()
print(f"<article>\n{content}\n</article>")

while (comment := input()) != "end of comments":
    print(f"<div>\n{comment}\n</div>")

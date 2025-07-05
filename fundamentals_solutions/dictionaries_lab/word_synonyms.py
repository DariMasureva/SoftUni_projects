pairs = int(input())
synonym_dict = {}

for _ in range(pairs):
    word, synonym = input(), input()
    synonym_list = synonym_dict.get(word)

    if synonym_list:
        synonym_list.append(synonym)
        synonym_dict[word] = synonym_list
    else:
        synonym_dict[word] = [synonym]


for word, synonyms in synonym_dict.items():
    print(f"{word} - {', '.join(synonyms)}")

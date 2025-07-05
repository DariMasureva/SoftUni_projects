initial_input = input().split()
count_dictionary = {}

for word in initial_input:
    word = word.lower()
    count_dictionary[word] = count_dictionary.get(word, 0) + 1

count_dictionary = {word: count for word, count in count_dictionary.items() if count % 2 == 1}
print(" ".join(count_dictionary.keys()))

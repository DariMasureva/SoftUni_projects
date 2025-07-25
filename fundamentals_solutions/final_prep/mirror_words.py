import re

all_pairs = input()
valid_pair_pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
# extracting the groups needed from the re results, making them into tuples
valid_pairs_found = re.findall(valid_pair_pattern, all_pairs)
valid_pairs = [(pair[1], pair[2]) for pair in valid_pairs_found]
# adding one of the words in the pair to the mirror list if the first is equal to the second reversed
mirror_pairs = [pair[0] for pair in valid_pairs if pair[0] == pair[1][::-1]]
if not valid_pairs:
    print("No word pairs found!")
else:
    print(f"{len(valid_pairs)} word pairs found!")
if not mirror_pairs:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for idx, mirror_word in enumerate(mirror_pairs):
        # all except the last pair should end in a comma
        if idx != len(mirror_pairs) - 1:
            print(f"{mirror_word} <=> {mirror_word[::-1]}", end=", ")
        else:
            print(f"{mirror_word} <=> {mirror_word[::-1]}")

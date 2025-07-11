text = input()
emoticon_idxs = [idx for idx, symbol in enumerate(text) if symbol == ":"]
emoticons = [text[idx:idx + 2] for idx in emoticon_idxs]

print("\n".join(emoticons))

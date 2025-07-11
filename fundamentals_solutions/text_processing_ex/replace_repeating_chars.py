keyboard_smash = list(input())

for idx, char in enumerate(keyboard_smash[1::], start=1):
    if char == keyboard_smash[idx - 1]:
        keyboard_smash[idx - 1] = ""

print("".join(keyboard_smash))

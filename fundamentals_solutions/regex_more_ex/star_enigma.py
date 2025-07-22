import re

messages_count = int(input())
destroyed = []
attacked = []
enigma_pattern = r"@([A-Za-z]+)[^@\-!:>]*:\d+[^@\-!:>]*!([A|D])![^@\-!:>]*->\d+"

for _ in range(messages_count):
    encrypted_message = input()
    # the value of the decryption key depends on how many times the letters of the word "star" are contained in the
    # encrypted message (case-insensitive)
    decryption_key = sum([1 for symbol in encrypted_message.lower() if symbol in "star"])
    # we should remove the decryption key value to the ascii of every symbol to decrypt
    # then I just join the whole list for convenience
    decrypted_message = "".join([chr(ord(symbol) - decryption_key) for symbol in encrypted_message])
    check = re.search(enigma_pattern, decrypted_message)

    if check:
        name = check.group(1)
        attack_type = check.group(2)

        if attack_type == "D":
            destroyed.append(name)
        else:
            attacked.append(name)

destroyed = list(sorted(destroyed))
attacked = list(sorted(attacked))

print(f"Attacked planets: {len(attacked)}")
for attacked_planet in attacked:
    print(f"-> {attacked_planet}")
print(f"Destroyed planets: {len(destroyed)}")
for destroyed_planet in destroyed:
    print(f"-> {destroyed_planet}")

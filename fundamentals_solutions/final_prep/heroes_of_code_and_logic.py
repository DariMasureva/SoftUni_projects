members_count = int(input())
party = {}

for _ in range(members_count):
    member_name, health, mana = input().split()
    party[member_name] = {"health": int(health), "mana": int(mana)}

while (command := input()) != "End":
    command_parts = command.split(" - ")
    action = command_parts[0]

    match action:
        case "CastSpell":
            member_name, mana_needed, spell_name = command_parts[1:]
            mana_needed = int(mana_needed)
            if party[member_name]["mana"] >= mana_needed:
                party[member_name]["mana"] -= mana_needed
                print(f"{member_name} has successfully cast {spell_name} and now has {party[member_name]['mana']} MP!")
            else:
                print(f"{member_name} does not have enough MP to cast {spell_name}!")
        case "TakeDamage":
            member_name, damage, attacker = command_parts[1:]
            party[member_name]["health"] -= int(damage)
            if party[member_name]["health"] >= 0:
                print(f"{member_name} was hit for {damage} HP by {attacker} and now has {party[member_name]['health']} HP left!")
            else:
                party.pop(member_name)
                print(f"{member_name} has been killed by {attacker}!")

        case "Recharge":
            member_name, amount = command_parts[1:]
            old_mana = party[member_name]["mana"]
            party[member_name]["mana"] = min(party[member_name]["mana"] + int(amount), 200)
            print(f"{member_name} recharged for {party[member_name]['mana'] - old_mana} MP!")
        case "Heal":
            member_name, amount = command_parts[1:]
            old_health = party[member_name]["health"]
            party[member_name]["health"] = min(party[member_name]["health"] + int(amount), 100)
            print(f"{member_name} healed for {party[member_name]['health'] - old_health} HP!")

for member_name, stats in party.items():
    print(f"{member_name}\n  HP: {stats['health']}\n  MP: {stats['mana']}")

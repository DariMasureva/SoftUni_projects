class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

party = Party()
while (person := input()) != "End":
    party.add_person(person)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

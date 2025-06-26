class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, animal_type, animal_species):
        if animal_type == 'mammal':
            self.mammals.append(animal_species)
        elif animal_type == 'fish':
            self.fishes.append(animal_species)
        else:
            self.birds.append(animal_species)

        Zoo.__animals += 1

    def get_info(self, animal_type):
        result = ""

        if animal_type == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif animal_type == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        else:
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
animals_count = int(input())

for _ in range(animals_count):
    animal_type_, animal_species_ = input().split()
    zoo.add_animal(animal_type_, animal_species_)

print(zoo.get_info(input()))

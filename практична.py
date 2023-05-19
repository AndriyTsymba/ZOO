import random
class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
        self.health = 100
        self.hunger = 0
        self.happiness = 100
    def grow(self):
        self.age += 1
        self.health -= random.randint(1, 10)
        self.happiness -= random.randint(1, 10)

    def eat(self):
        self.health += random.randint(5, 10)
        self.hunger -= random.randint(10, 20)
        self.happiness += random.randint(1, 10)

    def play(self):
        self.health -= random.randint(5, 15)
        self.hunger += random.randint(5, 10)
        self.happiness += random.randint(5,10)
    def __str__(self):
        return f"{self.species} - {self.name} - Age: {self.age}, Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}"
class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def remove_animal(self, animal):
        self.animals.remove(animal)
    def feed_all(self):
        for animal in self.animals:
            animal.eat()
    def play_with(self):
        for animal in self.animals:
            animal.play()
    def grow_all(self):
        for animal in self.animals:
            animal.grow()
    def __str__(self):
        zoo_description = "Zoo:\n"
        for animal in self.animals:
            zoo_description += str(animal) + "\n"
        return zoo_description
def save_zoo_state(zoo, day):
    with open(f"Day_{day}.txt", "w") as file:
        file.write(str(zoo))
zoo = Zoo()
lion = Animal("Lion", "Simba", 5)
giraf= Animal("Giraf", "Melmon", 3)
elephant = Animal("Elephant", "Dumbo", 2)
zoo.add_animal(lion)
zoo.add_animal(giraf)
zoo.add_animal(elephant)
for day in range(1, 11):
    save_zoo_state(zoo, day)
    print(f"Day {day}:\n")
    print(zoo)
    zoo.feed_all()
    zoo.play_with()
    zoo.grow_all()

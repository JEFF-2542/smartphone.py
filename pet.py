# Pet class representing a digital pet
class Pet:
    def __init__(self, name):
        self.name = name  # The pet's name
        self.hunger = 0  # Hunger level, where 0 = full and 10 = very hungry
        self.energy = 10  # Energy level, where 0 = tired and 10 = fully rested
        self.happiness = 5  # Happiness level, where 0 = sad and 10 = super happy
        self.tricks = []  # List to store the tricks the pet learns

    # Method to feed the pet, reducing hunger and increasing happiness
    def eat(self):
        if self.hunger > 0:
            self.hunger -= 3
            if self.hunger < 0:
                self.hunger = 0  # Hunger can't go below 0
            self.happiness += 1
            print(f"{self.name} is eating! Hunger level: {self.hunger}, Happiness level: {self.happiness}")
        else:
            print(f"{self.name} is not hungry right now.")

    # Method to make the pet sleep and regain energy
    def sleep(self):
        if self.energy < 10:
            self.energy += 5
            if self.energy > 10:
                self.energy = 10  # Energy can't exceed 10
            print(f"{self.name} is sleeping! Energy level: {self.energy}")
        else:
            print(f"{self.name} is already fully rested.")

    # Method to play with the pet, which affects hunger, energy, and happiness
    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
            if self.hunger > 10:
                self.hunger = 10  # Hunger can't exceed 10
            print(f"{self.name} is playing! Hunger level: {self.hunger}, Energy level: {self.energy}, Happiness level: {self.happiness}")
        else:
            print(f"{self.name} is too tired to play.")

    # Method to print the current status of the pet
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    # Bonus: Method to train the pet and teach it a new trick
    def train(self, trick):
        self.tricks.append(trick)
        self.happiness += 1  # Learning a trick increases happiness
        print(f"{self.name} learned a new trick: {trick}! Happiness increased!")

    # Bonus: Method to show all the tricks the pet has learned
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Creating an instance of the Pet class
my_pet = Pet("Buddy")

# Testing the methods
my_pet.get_status()  # Show initial status
my_pet.eat()  # Feed the pet
my_pet.sleep()  # Let the pet sleep
my_pet.play()  # Play with the pet
my_pet.train("Sit")  # Teach a trick
my_pet.train("Roll Over")  # Teach another trick
my_pet.show_tricks()  # Show the learned tricks
my_pet.get_status()  # Show final status after interaction

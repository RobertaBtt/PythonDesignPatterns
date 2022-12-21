import random


class Dog:
    def speak(self):
        return "I'm a dog"

    def __str__(self):
        return "doggy"


class Cat:
    def speak(self):
        return "I'm a cat. The best animal."

    def __str__(self):
        return "kitten"


class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "Food for dogs"


class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "Food for beautiful cats"


def get_factory():
    return random.choice([DogFactory, CatFactory])


class PetShop():
    def __init__(self, animal_factory = None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        pet.speak()
        self.pet_factory.get_food()

class Animal:
    babies = 0 

    def reproduce(self):
        self.babies += 1

#This is how you would overload in a python class
    def eat(food, amount=None):
        if amount is None:
            return f"{food} eaten. Nom."
        else:
            return f"{amount} {food} eaten. Nom."

#This is an example of overiding a function
class Dog(Animal):
    def reproduce(self):
        self.babies += 6


spot = Dog()
spot.reproduce()
print(spot.babies)

## Abstraction
# Abstraction allows us to create the lowest level blueprint
# of a class without anyone being able to create an instance of that class.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Mammal(Animal):
    def eat(self):
        return "Nom nom"

## Tutorial
# The superclass is going to be Bird.

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

## First subclass
class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck peck"
    
# used Polymorphism to override the reproduce method,
# Abstraction with the eat method 
# and Inheritance in this child class.

## Second Subclass
class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1
# used Polymorphism to override the reproduce method and Fly and extinct variables
# Encapsulation to keep the babies variable from being directly accessed

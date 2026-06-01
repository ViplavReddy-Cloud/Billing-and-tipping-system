def petlover(pet):
    pet.talk()
    if hasattr(pet, 'walk'):
       pet.walk()

class Duck:
    def talk(self):
        print("duck can talk")

    def walk(self):
        print("Duck can walk")

class Dog:

    def talk(self):
        print("Dog can talk")

    def walk(self):
        print("Dog can walk")

d = Duck()
petlover(d)

D =  Dog()
petlover(D)

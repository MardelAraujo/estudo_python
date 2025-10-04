class Animal:
    def fazerSom(self):
        pass
    
class Cachorro(Animal):
    def fazerSom(self):
        return "Au"

class Gato(Animal):
    def fazerSom(self):
        return "Miau"

class Pato(Animal):
    def fazerSom(self):
        return "Quack"

def fazerAnimalFalar(animal):
    return animal.fazerSom()
    
animal1 = Cachorro()
animal2 = Gato()
animal3 = Pato()

animais = [animal1, animal2, animal3]

for item_animal in animais:
    print(item_animal.__class__.__name__, fazerAnimalFalar(item_animal))
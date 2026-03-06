#objects 
class Person:
    species = "Homo sapien"

    def __init__(self, name, age):
        self.name = name
        self.age=age
    
    def introduce(self):
        return f"hi, im {self.name} and {self.age} years old"
    
    def have_birthday(self):
        self.age += 1
        return f"happy birthday, you are now {self.age} year old"
    
#objects
Person1 = Person("azim",25)
Person2 = Person("bob", 34)

print(Person1.name)
print(Person2.age)

print(Person1.introduce())
print(Person2.have_birthday())

print(Person.species)
print(Person1.species)

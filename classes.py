# class Person:
#     def __init__ (self,name):
#         self.name = name

#     def say_hi(self):
#         print("Hello, my name is", self.name)

# p = Person("Nick")
# q = Person("Tori")
# p.say_hi()
# q.say_hi()


class Dog:
    #class variable
    animal = "dog"

    #init method or constructor
    def __init__(self,breed,weight):
        #instance variables
        self.breed = breed
        self.weight = weight

    def attributePrinter(self):
        print("I am a", self.breed)
        print("I weigh", self.weight, "pounds")

Rodger = Dog("Husky",24)
print("Rodger is a", Rodger.animal) #class variable is accesssible to all chracters of a class
Rodger.attributePrinter()

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


cat1 = Cat("Andy", 2)
cat2 = Cat("Phoebe", 3)

cat1.info()
cat1.make_sound()

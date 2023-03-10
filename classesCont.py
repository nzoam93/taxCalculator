class Dog:
    def __init__(self, name, age, weight, characteristic):
        self.name = name
        self.age = age
        self.weight = weight
        self.characteristic = characteristic

    def info(self):
        print(f"I am {self.name}. I am {self.age} years old and weigh {self.weight} pounds. I am a {self.characteristic}")

    def makeSound(self):
        print("Woof")

Bean = Dog("Bean", 9, 45, "cutie")
Luna = Dog("Luna", 2.4, 15, "a good digger and a cutie")

Bean.info()
Bean.makeSound()

Luna.info()

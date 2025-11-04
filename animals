class Animal:
    def speak(self):
        print("Animal says: hello")
    def display(self):
        print("My name is Frank!")
    def move(self):
        print("running!")

class Baby(Animal):
    def speak(self):
        print("Baby says: Dad")
    def display(self):
        print("The baby is cute!")
    def move(self):
        print("crawl")

class Cow(Animal):
    def speak(self):
        print("Cow says: Moo")
    def display(self):
        print("I am black and white!")
    def move(self):
        print("I move slow sometimes!")

class Aardvark(Animal):
    def speak(self):
        print("Aardvark says: I don't make noise!")
    def display(self):
        print("I am ungly looking!")
    def move(self):
        print("I walk funny!")

class Person:
    def speak(self):
        print("Person says: I talk a lot!")

def animal_attributes(a):
    if not isinstance(a, Animal):
        print('\n--- Not an animal! ---')
        return
    a.speak()
    a.move()
    a.display()

animal = Animal()
baby = Baby()
cow = Cow()
aardvark = Aardvark()
person = Person()

animal_attributes(animal)
animal_attributes(baby)
animal_attributes(cow)
animal_attributes(aardvark)
animal_attributes(person)
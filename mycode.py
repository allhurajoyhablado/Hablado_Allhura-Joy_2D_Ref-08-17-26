class Profile:
    def __init__(self):
        self.name = "Allhura Joy Hablado"
        self.age = 22
        self.address = "Calantas, Floridablanca, Pampanga"
        self.favorite_color = "Purple"

    def display(self):
        print("I am " + self.name + ". I'm " + str(self.age) + " years old, and I live in " + self.address + ". My favorite color is " + self.favorite_color + ".")

profile = Profile()
profile.display()

class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound")

class dog(animal):
    def speak(self):
        print(f"{self.name} barks")

animal1=animal("Generic Animal")
dog1=dog("Buddy")

animal1.speak()
dog1.speak()
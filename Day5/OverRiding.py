class Animal:
    def sound(self):
        print("Animals makes sound")
class Bull(Animal):
    def sound(self):
        print("Bull Roar")
class Cat(Animal):
    def sound(self):
        print("Cat meows")

onbj =[Bull(), Cat()]
for i in onbj:
    i.sound()
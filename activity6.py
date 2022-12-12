Abstraction
Encapsulation
Polymorphism
Inheritance
student1 = {
    "name":"drake",
    "marks": 99
}
student2 = {
    "name": "Joey",
    "marks": 100
}
Classes and Objects
Python object can have multiple trait

callable (e.g. functions and classes)
iterable (e.g. list,string, generator)
contextable (e.g. files)

class person:
    pass
P=person()
print(P)
<__main__.person object at 0x000002AC061517E0>
hex(id(P))
'0x2ac061517e0'
a=1
 def square(a): 
    return a**2
class Person:
    name ="Drake"
    def say_hi(self):
        print(f"Hey There, I am {self.name}")
p =Person() # Method Call
p.say_hi() # Funcion Call     
Hey There, I am Drake

The __init__ method
Dunders (Event Methods)
class A:
    def __init__(self):
        print(self)
        print("Initialized")
    def __del__(self):
        print(self)
        print("I am Dying")
a=A()   
<__main__.A object at 0x0000028A87F92D40>
Initialized
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hello, my name is", self.name)
p = Person("Drake")
p.say_hi()
Hello, my name is Drake
a=1
a+1
2
a=1
a.__add__(5) 
6
"Drake" *2
'DrakeDrake'
"Drake".__mul__(2)
'DrakeDrake'
class A:
    a = 1
    b = 2
    def __add__(self,x):
        return self.a + self.b + x
a = A()
a + 3 
6

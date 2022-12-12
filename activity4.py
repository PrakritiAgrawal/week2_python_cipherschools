Functions
- Functions are reusebale blocks of codes/programs.
- We give names to the functions, to call it any number of times to run the block of the   code, this is known as Calling the function.
- range(), len() are some built-in functions we already used.

def show_loading():
    for i in range(a):
        print("Loading...")
a=int(input())
show_loading()     
Loading...
Loading...
Loading...
Function parameters
- Functions can take parameters.
def knock_drake(name):
    for _ in range(3):
        print("Knock knock",name)
knock_drake("Frank")     
Knock knock Frank
Knock knock Frank
Knock knock Frank
Return Statement
def add(a,b):
    return a + b
x=add(19,2)
print(x)
21
Keyword arguments
Giving values for parameters which are more by naming them is called keyword arguments
def func(a,b=5,c=10):
    print("a is",a,"and b is",b,"and c is ",c)
func(3,2)
a is 3 and b is 2 and c is  10
func(25,c=19)
a is 25 and b is 5 and c is  19
func(2,9,2)
a is 2 and b is 9 and c is  2
func(c=25,a=12)
a is 12 and b is 5 and c is  25
Arguments that are given in the function are called Formal Arguments, and the arguments that are given after execution is called Actual Arguments.
Positional mapping of arguments is perfomed while execution.
def hello():
    return 1
hello
hello()
1
Arguments in Python
Required arguments
Default arguments
Optional positional arguments
Required keyworded arguments
Default keyworded only arguments
Optional keyworded only arguments
# Required Arguments
def func(a,b):
    print(a,b)
func(1,2)
1 2
# Default Arguments
def func(a=10,b=20):
    print(a,b)
func()
func(1)
func(1,3)
10 20
1 20
1 3
# Optional Positional Only Arguments
def func(*a):
    print(a)
func(1,2,3,4,5,6,)
(1, 2, 3, 4, 5, 6)
def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,"hey",1.64)
1
2
(3, 'hey', 1.64)
def func(a,b,*c,d,e="heuy"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1,2,45.6,1,22,d=4) 
1
2
(45.6, 1, 22)
4
heuy
# Optional keyworded arguments 
def func(**k):
    print(k)
func()
func(name="joey")
{}
{'name': 'joey'}
def func(a,b=1,*c,d,e="",**k):
    print()
Anonymous Functions Or Lambda Functions
lambda a,b:a + b
b)>
_(2,4)
6
Lambda Expressions
lambda a,b:a+b     
(a, b)>
a=lambda a,b:a+b
a(4,9)  
13
Packing and Unpacking Values
a=[1,4]
b,c=a
print(b,c) 
1 4
names=("joey","pheobe","Ross")
for name in enumerate(names):
    print(name)   
(0, 'joey')
(1, 'pheobe')
(2, 'Ross')
names=["Joey","Drake","Rachel","Pheebs"]
scores=[99,85,78,100]
for name,score in zip(names,scores):
    print(name,"-",score)   
Joey - 99
Drake - 85
Rachel - 78
Pheebs - 100

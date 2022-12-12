# Tuples
Tuples are used to hold multiple objects.
Unlike lists Tuples are immutable i.e. you cannot modify tuples.
a=(1,2,3,4)
type(a)
tuple
a
(1, 2, 3, 4)
def func(*args):
    print(type(args))
func(1,2,3,4)
a=2
b=8
c=a,b
print(type(c))
def sum_diff(a,b):
    s=a+b
    d=a-b
    return s,d
sum_diff(1,3) 
(4, -2)
List to tuple and tuple to List:
a=(1,2,3,4)
list(a)
[1, 2, 3, 4]
tuple(a)
(1, 2, 3, 4)
Dictionary
a={""}
a={"name":"Drake"}
a["name"]
'Drake'
a={
    "name":"Joey",
    "Company":"Meta",
    "College":"LPU"
}
a["College"]
'LPU'
Dict Operations
key= "marks"
if key in a:
    print(a[key])
else:
    print("Key doesn't exist")
Key doesn't exist
key = "marks"
print(a.get(key)) 
None
key ="marks"
print(a.get(key, "key doesn't exist"))
key doesn't exist
a.values()
dict_values(['Joey', 'Meta', 'LPU'])
a.keys()
dict_keys(['name', 'Company', 'College'])

for key, value in a.items():
    print(key, "-->",value)
name --> Joey
Company --> Meta
College --> LPU
a
{'name': 'Joey', 'Company': 'Meta', 'College': 'LPU'}
"name" in a
True
for x in a:
    print(x)    
name
Company
College
 list(a)
['name', 'Company', 'College']

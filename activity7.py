Sets
Sets are unordered colections of simple objects and cannot be indexed
a={1,2,3,4,5}
a
{1, 2, 3, 4, 5}
list(a) 
[1, 2, 3, 4, 5]

a.add(24)
for i in a:
    print(i)
1
2
3
4
5
24
a={1,2,3,4}
b={3,4,5,6}
a-b 
{1, 2}
a.union(b)
{1, 2, 3, 4, 5, 6}
a.intersection(b)
{3, 4}
a.remove(4)
a=[['']*3]*3
a[1][1]="X"
[['', 'X', ''], ['', 'X', ''], ['', 'X', '']]
print(id(a[0][1]))
print(id(a[1][1]))
print(id(a[2][1])) 
2575972740144
2575972740144
257597274014
a=245
b=245
print(a is b)
True
is checks the memory address of the value.
a=(1,2,3,4)
hash(a)  
590899387183067792
Comprehension
a = []
for i in range(5):
    a.append(i)
print(a)
[0, 1, 2, 3, 4]
List Comprehension
[i for i in range(5) ]
[0, 1, 2, 3, 4]
a=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
[[j for j in range(5)] for i in range(5)]
[[0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4]]
[  to   ... ...]
a=[]
for i in range(2):
    for j in range(2):
        a.append(j)
print(a)
[0, 1, 0, 1]
n=5
[[max(i+1,j+1,n-i,n-j) for j in range(n)] for i in range(n)]
[[5, 5, 5, 5, 5],
 [5, 4, 4, 4, 5],
 [5, 4, 3, 4, 5],
 [5, 4, 4, 4, 5],
 [5, 5, 5, 5, 5]]
Dict Comprehension
{
    2:4,
    3:9,
    4:16
}
{2: 4, 3: 9, 4: 16}
{i: i**2 for i in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
Set Comprehension
a={ i for i in range(5)}
type(a)
a  
{0, 1, 2, 3, 4}
Generator comprehension
a = ( i for i in range(5))
type(a)
generator
for x in a:
    print(x)
0
1
2
3
4

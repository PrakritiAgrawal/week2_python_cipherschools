Lists
List is a data structure that holds an ordered collection of items i.e. you can store a sequence of items in a list.
--> List=[ ]

a=[1,2,3,4,5]
print(a)
[1, 2, 3, 4, 5]
b=["hey",2,1.5,4+3j]
print(b)     
['hey', 2, 1.5, (4+3j)]
a[0]=100
print(a)
[100, 2, 3, 4, 5]
Basic Operations
len([1,2,3,4,5])     
5
[1,2,3,4]+[5,6,7,8]     
[1, 2, 3, 4, 5, 6, 7, 8]
[2]*4     
[2, 2, 2, 2]
 a = [1,2,3,4,6]
 for x in a:
    print(x)     
1
2
3
4
6
"a" in "Hello"     
False
1 in [1,2,3,4]     
True
# Indexing and List Slicing
a= [1,2,3,4,5]
a[-1]     
5
a[0]    
1
# Updating the list
insert
append
a=[1,2,3,4,5]
a.insert(1,100)
a     
[1, 100, 2, 3, 4, 5]
a=[1,2,3,4,5]
a.append(6)
a     
[1, 2, 3, 4, 5, 6]
# Deleting list elements
del
pop
remove
a=[1,2,3,4]
a.pop()
a    
[1, 2, 3]
a=[1,2,3,4,5,6]
a.remove(1)
a    
[2, 3, 4, 5, 6]
# Sorting and Reversing
sort and sorted
reverse and reversed
a=[4,5,7,6,3,1,2,3]
a.sort()
a    
[1, 2, 3, 3, 4, 5, 6, 7]
b=[4,5,7,6,3,1,2,3]
sorted(b)    
[1, 2, 3, 3, 4, 5, 6, 7]
b    
[4, 5, 7, 6, 3, 1, 2, 3]
a=[1,2,3,4,5,6]
a.reverse()
a    
[6, 5, 4, 3, 2, 1]
b=[4,5,7,6,3,1,2,3]
list(reversed(b))    
[3, 2, 1, 3, 6, 7, 5, 4]
b    
[4, 5, 7, 6, 3, 1, 2, 3]
# Map Method
a=[1,2,3,4,5]
for x in (map(lambda x: x**2,a)):
    print(x) 
1
4
9
16
25
a=list(map(int, input().split()))
print(a) 
[12345]
type(a[0])
int
.join()

",".join(["Drake","Ramoray","Joey"])     
'Drake,Ramoray,Joey'

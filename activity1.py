# String Operations
1.String Formatting or String Interpolation
a=5
print("Value of a is %d" %(a))
Value of a is 5
print("Value of a is {}".format(a))    
Value of a is 5
a,b,c,d=1,2,3,4
"a {1}, b {2}, c {0}".format(c,a,b)
  output   'a 1, b 2, c 3'
name="Joey"
company="friends"
"Hello {name}, I'm an actor in the series {company}".format(name=name,company=company)  
"Hello Joey, I'm an actor in the series friends"
print(f"value of a is {a}")   
value of a is 5
len("a\nb")
output     
3
len(r"a\nb")     
4
 for c in "a\nb":
    print(c)
    
a

b

Strip method

"   Frank   ".strip()   
'Frank'
Split method

"1,2,3,4,5".split(",")
     
['1', '2', '3', '4', '5']
Replace method

"Joey Tribbiani".replace("i","o")
    
'Joey Trobboano'
Word Count

"Drake ramoray".count("r")


     
3

#CHAPTER-4 :- Dictonary & Sets

#Dictionary in Python
"""Dictionaries are used to store data values in key:value pairs 
They are unorderes, mutable(changeable)& don't allow duplicate keys"""


dict = {
    "name" : "Jamish",
    "cgpa" : 9.6,
    "marks" : [98, 97, 95],
    "learning" : "cooding",
    "subject" : ["python", "C", "Java"],
    "topics"  : ("Dictioanary", "sets"),
    "age" : 28,
    "is adult" : True,
    4 : 0
}

print(dict)
print(dict["name"])
print(dict["age"])
print(dict["subject"])

dict["name"] = "JamishSidd" #we can change of value only
dict["suname"] = "Sidd" # we can add key & value
print(dict)

null_dict = {} #we can create null_dict & add key: value
null_dict["jamish"] = "Sid"
print(null_dict)

#Nested dictionary
student = {
    "name" : "Jamish sidd",
    "subject" : {
        "phy" : 89,
        "chem" : 93,
        "math" : 96

    }
}



print(student["subject"]) # square bracket uses for subject & Chem is important
print(student["subject"]["chem"])

#self
student = {
    "name" : "JS College",
    "subject" : {
        "phy" : 89,
        "chem" : 93,
        "math" : 96,
        "roll no" : {
            "s-1" : 1128,
            "s-2" : 1129,
            "s-3" : 1130
        }

    }
}


print(student)
print(student["subject"])
print(student["subject"]["chem"])
print(student["subject"]["roll no"]["s-2"]) 

# Dictionary Methods

#Method-<1> <keys> Returns all keys except nested key
print(student.keys()) #nested key not showing only outer key

print(list(student.keys()))
print(tuple(student.keys()))
print(len(student.keys()))

#Method-<2> return all values
#data can stored into another data type
#Like : List store into dict and dict store into list{<ex: sub> under the list}

print(student.values())
print(list(student.values()))

#Method-<3> return all (key,value) pairs as tuples form

print(student.items())
print(list(student.items()))

student1 = {
    "name" : "JS College",
    "branch" : "mechanical",
    "samester-4" : "all subject",
    "subject" : {
        "phy" : 89,
        "chem" : 93,
        "math" : 96

    }
}

pairs = list(student1.items())
print(pairs[1])
print(pairs[2])

#Method-<4> return the key according to value

#(key method and .get method are same value output 
#but diff b/w key & .get : if mistake in value then key method is showing ERROR 
#and .get showing none).

print(student1["name"])
print(student1.get("name"))

#Method-<5> inserts the specified items to the dictionary

new_dict = {"city" : "delhi" , "age": 26}
student1.update(new_dict)
new_dict1 = {"samester-4" : "pass"}
student1.update(new_dict1)
print(student1)




#Sets :- 
#set is the collection of the unordered items
#Each elements in the set must be unique & immutable
#set is mutable
#set elements is immutable

# List & dictionary not stored in Set
# duplicate value is not allowe in Set 
# set() #empty set; SENTEX (empty dict{})
#duplicate value is not allowe in Set

collections = {1,2,3}
collection1 = {3,2,4,3,3,4,4,} 

print(collections)
print(collection1)



# Set Methods
#Method<1> -set.add(el) :- add an element

collection = set()

collection.add(2)
collection.add(3)
collection.add("learn coding")
collection.add((1,2,"good",))
print(collection) 

#Method<2> -set.remove(el) :- removes the element

collection2 = {1,2,3}
collection2.remove(2)
print(collection2)

#Method<3> -set.clear(el) :- empties the set

collection2.clear()
print(collection2)

#Method<4> -set.pop(el) :- removes a random value

collection3 = {1,2,"apna college", "world", "coding", "python"}

print(collection3.pop())

#Method<5> -set1.union(set2) :- Combines both set values & returns new set

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))

#Method<6> -set1.intersection(set2) :- Combines Common values & returna new set

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.intersection(set2))

#practice-1 :-
#Q- Store following word meaning in a python dictionary :

dict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}

print(dict) 

#practice-2 :- 

#Q :- you are given a list of subject  for students.
#Assume one classroom is required for 1 subject.
#How many classroom are needed by all students.

subject = {
    "python", "java", "C++", "python", "javascipt",
    "java", "python", "java", "C++", "C"
}

print(subject)
print(len(subject))
print(type(subject))

#practice-3
#Q:- WAP to enter marks of 3 subject from the user and store them in a dictionary.
#Start with an empty dictionary & add one by one.
#Use subject name as key & marks as value

marks = {}
x = int(input("enter phy: "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math: "))
marks.update({"math" : x})

print(marks)
print(type(marks))

#practice-4
#Figure out a way to store 9 & 9.0 as separate values in the set.
#(you can take help of bulit-in data type)

#sol-1 :- int & string 
value = {9, "9.0"}
print(value)
print(type(value))

#sol-2 :- pairs store in the tuple
value = {
    ("float", 9.0),
    ("int", 9)
}

print(value)

#[{(CHAPTER-<5>)}] 

#LOOPS in Python :- Loops are used to repeat instructions
#two types of loops <1> :- while loop & <2> :- for loop

#while loop ;- (val): in loop is called iterator
     # iteration : is run of program in loop, this process is called iteration

count = 1
while count<=5 :
    print("hello")
    count += 1

    i = 1

while i <= 10:
    print("apna college", i) #run with iterator (i)
    i+=1

j = 1
while j <= 8:
    print(j)
    j += 1

k = 5

while k >= 1:
    print(k)
    k -=1 

#Q-1 :- print numbers from 1 to 100

i = 1
while i <=100 :
    print(i)
    i +=1

#Q-2 :- Print numbers from 100 to 1

j = 100
while j >=1:
    print(j)
    j -= 1

#Q-3 :- print the multiplication table of a number n.

i = 1
while i<=10 : 
    print(3*i)
    i += 1

#from user input

n = int(input("enter number :"))
i = 1
while i<=10 : 
    print(n*i)
    i += 1

#Q-4 :- print the element of the following list using a loop:
# [1, 4, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
heroes = ["Thor", "Captain", "hulk", "loki"]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1

idx = 0 
while idx < len(heroes):
    print(heroes[idx]) # [ squre brackets using in this]
    idx += 1

#Q-5 :- Search for a number x in this tuple using loop:

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i = 0 
while i < len(num):
    if (num[i] == x):
        print("found at idx", i)
    i += 1 
    
#Break & Continue loop: (key words)
#<Break loop > :- used to trminate the loop when encountered

i = 1

while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

    num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i = 0 
while i < len(num):
    if (num[i] == x):
        print("found at idx", i)
        break
    i += 1

#<Continue loop > :- terminates execution in the current iteration & 
    #continues execution of the loop with the next iteration.

i = 0

while i <= 5:
    if(i == 3):
        i += 1
        continue # 3 will terminate
    print(i)
    i += 1

i = 0
#odd number 
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue # 3 will terminate
    print(i)
    i += 1

i = 11
#even number 
while i <= 20:
    if(i%2 != 0):
        i += 1
        continue # 3 will terminate
    print(i)
    i += 1

# for loop :- loops are for sequential traversal.
           # For traversing list,string,tuples.etc.

num = [1, 2, 3, 4, 5]

for val in num: # in is key word
    print(val)

city = ["delhi", "mumbai", "bihar", "hydrabad"]

for el in city:
    print(el)

str = "apna college"

for ch in str:
    print(ch)
             
str = "apnacollege"

for ch in str:
    if(ch == "o"):
        print("ok o found")
        break
    print(ch)
else:
    print("loop end")

#Q-1 (using for) print the elements of the following list using a loop
       # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in num:               #linear search
    print(val)

#Q-2 :- Search for a number x in this tuple using loop:
        #[1, 4, 9, 16, 25, 36, 49, 64, 81, 49, 100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 49, 100)

x = 49
idx = 0
for el in num:
    if(el == x):
        print("found at idx", idx)
        break # if skip another 49 then use break
    idx += 1


#Range(): :- Range function a sequence of numbers,starting from 0 by default,
          # and increments by 1 (by default), and stops before a specified number.

# <Range(start?, stop, step?)> :- 
#starting value is optional
#stoping value compulsry
#step size optional( by default start to 1)

for i in range(5):
    print(i)

    for i in range(10):
        print(i)

for i in range(2,10): # range( start, stop)
    print(i)

for i in range (2, 10, 2): #(start, stop , step)
    print(i)

#Q-1 :- Print numbers from 1 to 100.

for i in range(1,101):
    print(i)

#Q-2 :- print numbers from 100 to 1

for i in range(101,0, -1): 
    print(i)

#Q-3 :- print the multiplication table of a number n.

n = int(input("enter number : "))

for i in range(1, 20):
    print(n*i)

#Pass Statement :- pass is a null statement that does nothing.
                 #It is used as a placeholder for future code.

for i in range(5):
    pass
print("some work continue ")

#Q-4 :- WAP to find the sum of first n natural numbers. (using while)

n= 5
sum = 0
i = 1

while i <= n:
    sum += i
    i +=1 

print("total number =", sum)

# Sol-2 using for
n = 5
sum = 0

for i in range(1, n+1):
    sum += i

print("Total number =", sum)

#Q-5 :- WAP to find the factorial of first n natural number. (using for)

#sol-1 :- using for loop
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial =", fact)


#sol-2 using while loop

n = 5
fact = 1 # never put 0 
i = 1

while i <= n:
    fact *= i
    i += 1

print("factorial =", fact)




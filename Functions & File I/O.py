#[{{CHAPTER-<6>}}]

#Functions :- Block of statements that perform a specific task
# two types of functions:- <1>.Built in functions & <2>. User defind functions
#built in function :- print(), len(), type(), range()
#user defined function :- we create this function are user defined.

def calc_sum(a, b): #parameters
    sum = a + b 
    print(sum)
    return sum

calc_sum(5,10) #function call, (5,10)- arguments
#some work  

calc_sum(9,9)
#when requred calc call
calc_sum(1,9)
calc_sum("jam", "nuz")

def print_hello():
    print("hello")

print_hello()

print_hello()

#average of 3 numbers

def cal_avg(a,b,c):
    sum = a + b + c 
    avg = sum/3
    print(avg)
    return avg


cal_avg(20,30,40)

# Default parameters :- Assigning a default value to parameter, which is used when no argument is passed.




def cal_prods(a=1,b=2):
    print(a*b)
    return a*b

cal_prods()


def cal_prod(a,b=2):
    print(a*b)
    return a*b

cal_prod(1)

#Q-1 :- WAF to print the length of a list.(list is the parameter)

cities = ["delhi", "mumbai", "bihar", "up", "kolkata"]
heroes = ["Thor", "batman", "Hulk", "superman", "ragnar"]

def list_len(list):
    print(len(list))
    

list_len(cities)

list_len(heroes)

#Q-2 :- WAF to print the elements of a list in asingle line.(list is the parameter)

heroes = ["Thor", "batman", "Hulk", "superman", "ragnar"]

def print_list(list):
    for item in list:
        print(item, end = " ")


print_list(heroes)

#Q-3 :- WAF to find th factorial of n. (n is the parameter)

#using of loops for revised & simplify
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i 
    print(fact)

cal_fact(5)

#Q-4 :- WAF to convert USD to INR

#sol-1 own

def usd(n):
    inr = 83
    for i in range(1,n+1):
        inr *= i
    print(inr)

usd(1)

#sol-2 :- right way of SYNTEX

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val,"USD =", inr_val, "INR")

converter(1)

#Q-5 :- WAP n number is odd than output is odd & if number is even 
#than output even strng (Using function)

def cal(a):
    if a%2 == 0:
        print("even")
    elif a%2 != 0:
        print("odd")

cal(9)

#RECURSION :- When a function cells itself repeatedly

def show(n):
    if(n == 0): #base case 
        return
    print(n)
    show(n-1)

show(5)

#factorial :-
 
def fact(n):
    if (n == 1 or n == 0):  #base case(vvp)
        return 1
    return fact(n-1)* n

print(fact(5))

#Q-1 :- Write a recursive function to calculate the sum of first 
# n natural numbers.

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

# Write a recursive function to print all elements in a list
#HINT : use list & index as parameters.

def list_f(list,idx =0):
    if (idx == len(list)):
        return 
    print(list[idx])
    list_f(list, idx+1)

fruits = ["Apple", "Banana", "Litchi", "Mango"]
list_f(fruits)

#[{{CHAPTER-<7>}}] :- File I/O (input/output) in Pyhton
# Pyhton can be used to perform operations on a file.(read & write data)
#types of all files :- 1> Text file : .txt, .docx, .log etc.
                      # 2> Binary files : .mp4, .mov, .png, .jpeg etc.
                      
#read:

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
#f.close()

f = open("demo.txt","r")
data = f.read(5)         # we can number of character specified
print(data)
print(type(data))

#readline:

f = open("demo.txt","r")
line1 = f.readline()
print(line1) 

f = open("demo.txt","r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

#Write:

f = open("demo.txt", "w")
f.write("I want to learn SQL Tonight.123")
f.close()

f = open("demo.txt", "a")
f.write("\nAfter that learn cloud computing")
f.close()

# if we creat file use to code:

f = open("Sample.txt", "w") #we can use (a) append also
f.close()

# r+ : mode : read + overwrite (pointer is starting point)
# in this case : no truncate

f = open("demo.txt","r+")
f.write("abc")
f.close()

# w+:mode : read & write 
# in this case : truncate (no matter pointer)

f = open("demo.txt","w+")
f.write("SQL")
print(f.read())
f.close()

# a+ : mode: read + append (pointer end)
# in this case : no truncate

f = open("demo.txt","a+")
f.write("start")
print(f.read())
f.close()

# WITH STNTAX;

with open ("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("new data")

# Deleting file

import os

os.remove("Sample.txt")

# Q-1 :- Create a new file "pratice.txt" using python. Add
#the following data in it:

"""Hi everyone
   we are learning File I/O
   using Java.
   I like programming in Java."""

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

# Q-2 :- WAF that replace all occurences of "Java" with "python"
# in above file.

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# Q-3 :- Search if the word "learning" exist in the file or not.

def check_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word)!= -1):
            print(("found"))
        else:
            print("not found")

check_word()

# Q-4 :-WAF to find which line of the does the word "learning"
# occur first. print-1 if word not found.

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1 
    return -1

print(check_for_line())

# Q-5 :-From a file containing numbers separated by comma,
# print the count of even number

# using list.split method
 
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)

print("end")




























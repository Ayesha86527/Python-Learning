#FUNCTIONS  (used to reduce redantancy)

"""def sum(a,b):
    sum=a+b
    print(sum)
    return sum 

sum(3,6)
sum(2,8)"""


"""def avg(a,b,c):
    avg=(a+b+c)/2
    print(avg)
    return avg

avg(9,4,8)"""

"""def  sum(a,b):         #Can also do like this
    return a+b

sum=sum(1,2)
print(sum)"""

"""def print_hello():
    print("hello")

output=print_hello()
print(output) """    #None


#For same line

"""print("hello",end=" ")
print("Ayesha")"""

#Default Parameters


"""def prod(a=3,b=3):
    print(a*b)
    return a*b
prod()

def sum(a,b=9):
    print(a+b)
    return a+b
sum(3)"""       #But it cannot be viceversa case


#Practice

"""def list(a):
    print(len(a))
    return len(a)
list("I am Ayesha")"""


#WAF to print the length of a list(list is the parameter)

"""cities=["Karachi","Lahore","Islamabad"]

def print_len(cities):
    print(len(cities))

print_len(cities)"""


#WAF to print the elements of a list in a single line

"""animals=["cat","dog","monkey","frog"]

def ele(animals):
    print(animals[0],end="\n")
    print(animals[1])
    print(animals[2])
    print(animals[3])

ele(animals)"""


#WAF to find the factorial of n.

"""n=3

def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print(factorial)

factorial(n)"""


#WAF to convert USD value into PKR

"""USD=float(input("Enter the amount:"))

def change(USD):
    change=USD*278.62
    print(change)
    return USD*278.62

change(USD)"""


#WAF to tell if a no is odd or even

"""a=int(input("Enter any no:"))
def tell(a):
    if(a%2==0):
        print("Even")
    else:
        print("Odd")
    print(tell)
    
tell(a)"""


"""def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
f=int(input("Enter any number:"))
print(fact(f))"""

#Fibonacci

"""def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+f(n-1)
    
no=int(input("Enter any number:"))
print(f(no))"""


N=int(input())
countries=set()

for i in range(1,N+1):
    C=input()
    countries.add(C)

print(len(countries))

    



        











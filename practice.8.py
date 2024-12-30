#For n=3 (2 spaces chorein ge first wale mein)

"""n=int(input("Enter any no:"))
for i in range(1,n+1):
  print(" "* (n-i),end="")
  print("*"* (2*i-1),end="")
  print("")"""


'''n=int(input("Enter any no:"))
for i in range(1,n+1):
  print(" "*(n-i),end="")
  print("*"*i,end="")
  print("")'''

"""
***
* *
***"""


"""n=int(input("enter any no:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")"""



#reverse table
"""n=int(input("enter any no:"))
for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}"""


"""n=input("Enter your name:")
def greet(n):
    print("Hello",n)
greet(n)"""


"""def goodDay(name,ending):
    print("Good Day"+ name)
    print(ending)
    return "done"
a=goodDay("Ayesha","Thanks")
print(a)"""


"""def sum(a,b):
    plus=a+b
    print(plus)
    return "done"
a=sum(4,8)
print(a)"""


"""def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)


n=int(input("Enter the no:"))
fact(n)

print("The factorial of",n,"is",fact(n))"""


"""def g():
    n=int(input("Enter the first no:"))
    n1=int(input("Enter the second no:"))
    n2=int(input("Enter the third no:"))
    if(n>n1 and n>n2):
        print(n,"is the greatest number.")
    elif(n1>n2):
        print(n1,"is the greatest number.")
    else:
        print(n2,"is the greatest number.")

g()"""

"""import math
def con():
    t=int(input("Enter the temperature in celcius:"))
    f=32+1.8*t
    r=math.floor(f)
    print("The temperature in farenhiet is",r)

con()"""


"""def plus(n):
    if(n==1):
        return 1
    return n+plus(n-1)


n=int(input('Enter any no:'))
plus(n)
print("The sum of first",n,"numbers is",plus(n))"""


"""def pattern(n):
    if(n==0):
        return "nothing"
    print("*"*n)
    pattern(n-1)

n=int(input("Enter any no:"))
pattern(n)"""


"""def rem(l,word):
    for item in l:
        n=[]
        if not(item==word):
            n.append(item.strip(word))
        return n
        
l=["djdj","assbs","an"] 
print(rem(l,"ass"))"""


#1 for snake
#-1 for water
#0 for gun

"""import random

comp=random.choice([1,0,-1])
user=input("Enter your choice:")
dict={"s":1,"g":0,"w":-1}
rev_dict={1:"snake",0:"gun",-1:"water"}

you=dict[user]

print(f"You choose {rev_dict[you]}\nComputer choose {rev_dict[comp]}")

if(comp==you):
    print("It's a draw!")
elif(comp==1 and you==0):
    print("You Win!")
elif(comp==1 and you==-1):
    print("You lose!")
elif(comp==0 and you==-1):
    print("You Win!")
elif(comp==0 and you==1):
    print("You lose!")
elif(comp==-1 and you==0):
    print("You lose!")
elif(comp==-1 and you==1):
    print("You Win!")
else:
    print("Something went wrong")"""



A_count=0
B_count=0
C_count=0
D_count=0
F_count=0
sum=0
s=int(input("Enter the strength of class:"))
i=0
while i<s:
    marks=int(input("Enter the marks of student:"))
    if(marks>0 and marks<=100):
        sum=sum+marks
        i+=1
        if(marks>=85 and marks<=100):
          grade="A"
          A_count=A_count+1
        elif(marks>=75 and marks<=84):
          grade="B"
          B_count=B_count+1
        elif(marks>=65 and marks<=74):
          grade="C"
          C_count=C_count+1
        elif(marks>=55 and marks<=64):
          grade="D"
          D_count=D_count+1
        elif(marks<55):
          grade="F"
          F_count=F_count+1
    else:
       continue

print("Class Performance")
print(A_count,"students secured A grade.")
print(B_count,"students secured B grade.")
print(C_count,"students secured C grade.")
print(D_count,"students secured D grade.")
print(F_count,"students secured F grade.")
avg=sum/s
print("The class average is",avg)

    


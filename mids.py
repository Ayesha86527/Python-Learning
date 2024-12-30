#loops


#prints all numbers in one line
"""for i in range(11):
    print(i,end=" ")""" 

#prints cubes
"""for i in range(1,11):
    print(i*i*i,end=" ")"""


#returns squares in one line
"""l=[1,2,3,4,5,6]

for i in l:
    print(i*i,end=" ")"""

#returns list of squares
"""l=[1,2,3,4,5,6]

l1=[x*x for x in l]
print(l1)"""

#Factorial

"""n=int(input())
fact=1
for i in range(n,0,-1):
    fact=fact*i
print(fact)"""

#table

"""n=int(input())

for i in range(1,11):
    print(n,"*",i,"=",n*i)"""


"""A_count=0
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
print("The class average is",avg)"""


#1
#2 2
#3 3 3 
#so on...

"""for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()"""

#rows same
"""for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()"""

#colums same
"""for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()"""




#2 2 4 4 6 6 8 8 10 10

#1 2 3 4 5
#1 4 9 16 25
#1 8 27 64 125


"""for i in range(2,11,2):
    print(i,end=" ")
    print(i,end=" ")"""

"""for i in range(1,6):
    print(i,end=" ")
print()
for j in range(1,6):
    print(j*j,end=" ")
print()
for k in range(1,6):
    print(k*k*k,end=" ")
print()"""

#*
#**
#so on..
"""for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()"""

#*****
#****
#so on..

"""for i in range(6,0,-1):
    for j in range(i-1):
        print("*",end="")
    print()"""

#  *
# ***
#*****
#so on...

"""n=int(input())

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()"""

#*****
# ***
#  *

"""n=int(input())

for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()"""


#N

"""for i in range(1,11):
    for j in range(1,11):
        if j==1:
            print(1,end="")
        elif i==j:
            print(2,end="")
        elif j==10:
            print(3,end="")
        else:
            print(" ",end="")
    print()"""

#H

"""for i in range(1,11):
    for j in range(1,11):
        if j==1:
            print(1,end="")
        elif i==5:
            print(2,end="")
        elif j==10:
            print(3,end="")
        else:
            print(" ",end="")
    print()"""

#Z 

"""for i in range(1,11):
    for j in range(1,11):
        if i==1:
            print(1,end="")
        elif i==j:
            print(2,end="")
        elif i==10:
            print(3,end="")
        else:
            print(" ",end="")
    print()"""

#functions

#sum

"""def sum(a,b):
    return a+b

r=sum(2,3)
print(r)"""

"""def fact(n):
    fact=1
    if n==0 or n==1:
        return 1
    else:
        for i in range(1,n+1):
           fact=fact*i
        return fact
    
n=int(input())
r=fact(n)
print(r)"""

"""def tab(n):
    for i in range(1,11):
        print(i,"*",n,"=",i*n)

n=int(input())
tab(n)"""

#list sorting 

"""l=[89,45,78,90,23,68]

for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)"""



#recursions

"""def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
r=fact(5)
print(r)"""


""""def check(n):
    count=0
    ccount=0
    for i in n:
        if i in "aeiouAEIOU":
            print(i,"is found at",n.index(i))
            count=count+1
            print(i,"appears",count,"times in this phrase.")
        elif i==" ":
            continue
        else:
            print(i,"is a consonant found at",n.index(i))
            ccount=ccount+1
            print(i,"appears",ccount,"times in this phrase.")
a=input()
check(a)"""

#0
#11
#so on
"""for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()"""

"""i=0
n=int(input("Enter no of subs:"))
sum=0
while i<n:
    marks=int(input("Enter marks of sub:"))
    sum=sum+marks
    i+=1

avg=sum/n
print("You average is:",avg)"""

#naam ulte hojate
"""l=["apple","mango","banana","grapes"]
l1=[x[::-1] for x in l]
print(l1)"""

#s="abracadabra"
#slicing
"""print(s[2:7])
print(s[-9:-4])"""

#P1

"""for i in range(1,51):
    if i%3==0:
        print(i)
    else:
        continue"""

"""l=[i for i in range(1,51) if i%3==0]
print(l)"""

#P2

"""def check_even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

n=int(input())
r=check_even_odd(n)
print(r)"""


#P3

"""s="MidTerm2024"

print(s[0:3])
print(s[-4:])
print(s[::-1])"""

#P4

"""def sum_of_digits(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n%10+sum_of_digits(n//10)

n=int(input())
r=sum_of_digits(n)
print(r)"""


#P5

"""l=[4,9,1,6,2]

for i in range(0,len(l)):
    for j in range(0,len(l)-1):
       if l[j]>l[j+1]:
        temp=l[j]
        l[j]=l[j+1]
        l[j+1]=temp
print(l)

for k in l:
    if k==l[3]:
        print(k,"is the second largest number")"""


















        
    












    




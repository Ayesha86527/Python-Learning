#LCM
"""n1=int(input())
n2=int(input())
maxn=max(n1,n2)
while True:
    if maxn%n1==0 and maxn%n2==0:
        break
    maxn+=1

print("The LCM of",n1,"and",n2,"is",maxn)"""


#armstrong number
"""import math
n=input()

l=list(n)
fl=[]


for no in l:
        ln=math.pow(int(no),len(l))
        fl.append(ln)

print("The armstrong number of this number is",sum(fl))"""


#sum of matrix

"""def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
          inp=int(input(f"Enter o[{i}][{j}]"))
          row.append(inp)
        o.append(row)
    return o

def sum(A,B):
    output=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output

m=int(input("Enter the value of m/n"))
n=int(input("Enter the value of m/n"))

print("Enter matrix A")
A=matrix(m,n)
print(A)
print("Enter matrix B")
B=matrix(m,n)
print(B)

s=sum(A,B)
print(s)"""


#String operations

#string to list 
"""s="Ayesha"
l=[]
for i in s:
    l.append(i)
    
for j in l:
    print(j)
print(l[0])"""

#list to string join
"""l=["j","a","m"]
s="".join(l)
print(l)

l1=["jam"]
l2=[]
s=str(l)
for i in l:
    l2.append(i)

print(l2)"""


"""def vc(phrase):
    vcount = 0
    ccount = 0
    
    # Define sets of vowels
    vowels = "aeiouAEIOU"
    
    for char in phrase:
        if char in vowels:  # Check if character is a vowel
            vcount += 1
        elif char.isalpha():  # Check if it's a consonant
            ccount += 1
    
    return f"The total number of vowels in your phrase are {vcount} and total number of consonants are {ccount}."

# Get input from the user
phrase = input("Enter your phrase: ")
print(vc(phrase))"""

#anagram
"""w1=input("Enter word 1:")
w2=input("Enter word 2:")
if len(w1)==len(w2):
   s1=sorted(w1)
   s2=sorted(w2)
   if s1==s2:
    print(True)
   else:
    print(False)"""


#Slicing in strings

"""s="hello"

print(s[:5])
print(s[0:])
print(s[2:4])
print(s[0:4])
print(s[::-1])"""


"""l=[89,4,56,72,11,72]
l2=set(l)
l3=list(l2)

for i in range(len(l3)):
    for j in range(len(l3)-1):
        temp=l3[j]
        if l3[j]>l3[j+1]:
            l3[j]=l3[j+1]
            l3[j+1]=temp

print(l3)"""


"""l=[]
n=int(input())

for i in range(n):
    a=int(input())
    b=int(input())
    l.append((a,b))

for j in range(len(l)):
    print(sum(l[j]))"""


"""p=input()
dict={}

l=p.split()

for i in l:
    c=l.count(i)
    dict.update({i:c})

print(dict)"""


"""l=[12,78,34,12,4]

for i in l:
    for j in l:
        if i==j:
            l.remove(i)

print(l)"""

"""def stats(file):
    charc=0
    with open(file) as f:
        data=f.read()
        l=data.split()
        wordcount=len(l)
        f.seek(0)
        lines=f.readlines()
        nlines=len(lines)
        l2=list(data)
        for char in l2:
            if char==" ":
                continue
            else:
                charc+=1

    return f"The total number of words are {wordcount}, the total lines are {nlines} and total characters are {charc}"

file=input("Enter file path:")
print(stats(file))"""


"""def duplicate(file):
    with open(file) as f:
        data=f.read()
        for i in data:
            if data.count(i)>1:
                return True
            return False
        
file=input("Enter file path:")
print(duplicate(file))"""


"""n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()"""

"""n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()"""




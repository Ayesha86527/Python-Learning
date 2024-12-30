"""f=open("myfile.txt","w")
f.write("So ya everyone here is a donkey because i don't why but it is what it is! Everyone in the room is a donkey!")
f.close()"""

"""word="donkey"
f=open("myfile.txt")
content=f.read()
new_content=content.replace("donkey","###")

with open("myfile.txt","w") as f:
    f.write(new_content)"""


"""words=["bitch","fuck","hate"]

with open("myfile.txt") as f:
    con=f.read()
for word in words:
        con=con.replace(word,"#" * len(word))
with open("myfile.txt","w") as f:
      f.write(con)"""

#map
"""def cube(x):
    return x*x*x
l=[1,2,3,4,5]
newl=list(map(cube,l))
print(newl)"""

#filter

"""def filter_(a):
    return a>4
l=[1,2,3,4,5,6,7,8,9]
newl=list(filter(filter_,l))
print(newl)"""


#lambda

"""l=[1,2,3,4,5]
newl=list(map(lambda x:x+x,l))
print(newl)"""


#reduce

"""from functools import reduce

l=[1,2,3,4,5]

sum=reduce(lambda x,y:x+y,l)
print(sum)"""


"""phrase=input("Enter your phrase:")

vcount=0
ccount=0

for i in phrase:
    if i in "AEIOUaeiuo":
        print(i,"is a vowel and found at",phrase.index(i))
        vcount=vcount+1
    elif i==" ":
        continue
    else:
        print(i,"It's a consonant")
        ccount=ccount+1

print("Total vowels",vcount)
print("Total consonants",ccount)"""


""""def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
for i in range(1,11):
    print(i,"=!",fact(i)"""

"""n=int(input("Enter any no:"))
result=fact(n)
print(result)"""


"""fruits=[]

for i in range(5):
    item=input("Enter fruit name:")
    for i in item:
        if i[0] not in "MEG":
            fruits.append(item)
        else:
            continue
        print(fruits)  """ 

#matrix addition
"""l1=[1,2,3],[4,4,5],[2,2,2]
l2=[1,2,1],[3,4,4],[1,2,3]
l3=[0,0,0],[0,0,0],[0,0,0]


for i in range(0,len(l1)):
    for j in range(len(l1)):
        l3[i][j]=l1[i][j]+l2[i][j]
for i in l3:
    print(i)"""

"""l1=[67,45,12,34,89,3]

for i in range(0,len(l1)):
    for j in range(0,len(l1)-1):
        if l1[j]>l1[j+1]:
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
print(l1)"""


"""l1=[67,45,12,34,89,3]

print(l1[:3])
print(l1[:-3])"""

#jump

"""l1=[67,45,12,34,89,3]

print(l1[-2:-5:-1])
print(l1[-5:-2])"""


#match case

"""a=input()

match a.islower():
    case 1:
        print("Case is 1")
    case _:
        print("None")"""



"""def mutate_string(string,position,character):
    l=list(string)
    for i in l:
        if i==position:
             l.insert(i,character)
             return l
    
            
        

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)"""

"""n=input()


if (sub.isalnum() for sub in n):
    print(True)
else:
    print(False)
if (sub.isalpha() for sub in n):
    print(True)
else:
    print(False)
if (sub.isdigit() for sub in n):
    print(True)
else:
    print(False)
if (sub.islower() for sub in n):
    print(True)
else:
    print(False)
if (sub.isupper() for sub in n):
    print(True)
else:
    print(False)"""





    













    





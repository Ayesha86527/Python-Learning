"""import calendar

y=int(input("Enter year:"))
m=int(input("Enter month:"))

print(calendar.month(y,m))"""


"""first=input("Enter first name:")
last=input("Enter lasr name:")

print("Hi! My name is",last,first)"""


"""name=input("Enter yoyur name:")
age=int(input("Enter your age:"))

hundred=100-age
print(name,"will turn 100 years old after",hundred,"years")"""



"""T=float(input("Enter the temperature:"))

C=(T-32)/1.8
print("The temperature in celsius is",C)"""


"""x=float(input("Enter length:"))

y=float(input("Enter breadth:"))

print("The area of rectangle is",x*y)"""

"""import math
r=float(input("Enter the radius:"))
v=4/3*(math.pi)*(math.pow(r,3))

print("The volume of sphere is",v)"""


"""P=float(input("Enter the principal amount:"))
R=float(input("Enter the rate:"))
t=float(input("Enter the time span:"))
A = P*(1 + R/100)*t
C=A-P
print("The compound interest is",C)"""




"""l=[34.99,29.95,31.50]
print(max(l))"""


"""t=403//73
print(t,"times 73 goes into 403.")"""



"""r=0.2
angular_speed=12.56
v=r*angular_speed
t=10
distance=v*t
print("The distance is",distance)"""


"""u = 50 
a= 10      
t = 2              
distance_traveled = (u * t) + (0.5 * a * t ** 2)
print(distance_traveled)"""



"""import math
u = 0      
a = 32         
s= 100            
final_velocity = math.sqrt(u**2 + 2 * a * s)
print("The final velocity of the stone when it hits the ground is:", final_velocity)"""



"""r=float(input("Enter the radius:"))
angular_speed=523.3
v=r*angular_speed
print("The linear velocity is",v)"""
import math
"""a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

x1=((-b+math.sqrt(b**2-(4*a*c)))//2*a)
x2=((-b-math.sqrt(b**2-(4*a*c)))//2*a)

if a==0:
    print("The denominator is 0.")
else:
    print("x1:",x1,"x2:",x2)"""


"""n=int(input("Enter the number of terms:"))
a=int(input("Enter the first term:"))
d=int(input("Enter the common difference:"))
while True:
    an=a+(n-1)*d
    print(an)
    c=input("Do uou want to continue(Y/N):")
    if c=='Y':
        n=int(input("Enter the number of terms:"))
    elif c=='N':
        break"""

"""name=input("Enter your name:")
f_name=input("Enter your father's name:")
r=input("Enter your roll no:")
list=[]
for i in range(5):
    s=input("Enter the subject name with marks:")
    list.append(s)

print(name,"who is the S/O",f_name,"has secured the following marks:")
print("\n".join(list))"""


"""n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,6):
        print(i*j,end=" ")
    print()"""





"""m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,1,1],[1,1,1],[1,1,1]]
mul=[[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        for k in range(len(m2)):
            mul[i][j]+=m1[i][k]*m2[k][j]
for i in mul:
    print(i)"""


"""p=input("Enter the word:")
p.casefold()

if p==p[::-1]:
    print("YES!")
else:
    print("SORRY:(")"""
         

"""i=1
n=100

while i<=n:
    if i%2!=0:
        print(i)
        i+=1
    else:
        continue
    i+=1"""



"""lst=[int(x) for x in input().split()]
mi=len(lst)//2
print(mi)
m=lst[len(lst)//2]
print(m)
lst.sort(reverse=True)
print(lst)
lst.append(lst.pop())
print(lst)"""










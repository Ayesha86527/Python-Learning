#Write a python program to print the contents of a directory using os module

"""import os

print(os.listdir("downloads"))"""   #give contents of a directory

"""a="56.9"
b=float(a)
t=type(a)
print(t)"""    #type is not changed

#But if 
"""a="56.9"
b=float(a)
t=type(b)
print(t)"""      #Now type is changed


#Check the type of variable assigned using input function

"""v=input("Enter the variable:")
t=type(v)
print("The type of variable is",t)"""   #it will always give str no matter what weinput


#Slicing

"""a="AyeshaNoman"
print(a[0:6])
print(a[6:11])
print(a[-5:]) 

#skip value slicing

print(a[0:11:1]) """ #1=step

#Escaoe sequence character

"""a='I am Aashie and also Ashi\nbut not asho\tbut sometimes yeah'
print(a)
#\n=next line   \t=tab space

b='I am "18"'
print(b)"""

"""name=input("Enter your name:")
print("Good Afternoon!",name)"""

"""letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace('<|Name|>', 'Ayesha').replace('<|Date|>', '15 July 2025'))"""


#Write a program to detect double space in a string

"""a="Hey!  I am Ayesha."
print(a.find("  "))
print(a.replace("  ", " "))"""


"""letter="Dear Harry,\n\tThis python tutorial is awesome.\nThankyou!"
print(letter)"""



#We can also slice lists

"""list=['rr',9,'true','aisha','orange']

print(list[1:3])

list.remove("rr")
print(list)"""


#repeat a tuple

"""my_tuple=(1,2,3)
repeated=my_tuple*5
print(repeated)

print(2 in my_tuple)    #true
print(8 in my_tuple)"""   #false


#WAP to store seven fruits in a list entered by the user

"""a=input("enter fruit:")
b=input("enter fruit:")
c=input("enter fruit:")
d=input("enter fruit:")
e=input("enter fruit:")
f=input("enter fruit:")
g=input("enter fruit:")
list=[a,b,c,d,e,f,g]
print(list)"""

#WAP to accept marks of 6 students and display them in a sorted manner

"""s1=int(input("enter the marks:"))
s2=int(input("enter the marks:"))
s3=int(input("enter the marks:"))
s4=int(input("enter the marks:"))
s5=int(input("enter the marks:"))
s6=int(input("enter the marks:"))
list=[s1,s2,s3,s4,s5,s6]
list.sort()
print(list)"""


#WAP to sum a list 4 numbers

"""a=int(input("enter the no:"))
b=int(input("enter the no:"))
c=int(input("enter the no:"))
d=int(input("enter the no:"))
list=[a,b,c,d]
print(sum(list))"""


#WAP to count the number of zeros in the following tuple:

"""tup=(5,8,0,9,0,6,4,0)

print(tup.count(0))"""


    
















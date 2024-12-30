#Lists in Python 

"""marks=[98.7,95.4,78.6,65.9,65.4]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))"""

"""student=["Salar",100,"Islamabad"]
print(student[0])
student[0]="Chu Chu"
print(student)""" #Changing allowed in list

"""str="hello"
print(str[0])
str[0]="y"""   #Not allowed in string

#List Slicing

"""marks=[20,40,60,90,50]
print(marks[:3])   #Ending index is not included

print(marks[-5:-2]) """ #negative slicing

#List Methods

#Append Method

"""list=[1,2,3]
list.append(4)  #[1,2,3,4]
print(list)"""

#Sort Method

"""list=[7,3,9]
list.sort()  #[3,7,9](ascending)
print(list)"""

"""list=[6,9,7]
list.sort(reverse=True)  #descending order
print(list)"""

"""list=['a','t','r','h']
list.sort()    #Sorting is possiblr in strings too
print(list)"""

#Reverse Method

"""list=[9,6,4]
list.reverse()
print(list)"""

#Insert Method

"""list=["a","m","j","k","o"]
list.insert(2,"n")  #[a,m,n,j,k,o]
print(list)"""

#Remove Method

"""list=[8,9,7]
list.remove(9)
print(list)"""

#Pop Method

"""List=[8,9,7]
list.pop(1)
print(list)"""



#TUPLES

"""tup=(1,2,3,4,5)
print(tup[0])    #1
tup[0]=5 """        #This operation not allowed in tupules but allowed in lists

"""tup=(2,)        #For only one value we write like this so python can differiate between an int and a tuple
print(tup)"""

#Slicing
"""tup=(3,4,5)
print(tup[1:2])""" #4

#Methods in Tuples

#Index Method

"""tup=(9,2,8,4)
print(tup.index(9))"""    #0

#Count Method

"""tup=(2,4,5,4)
print(tup.count(4))"""




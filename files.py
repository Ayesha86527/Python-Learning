#Files I/O in Python

#Reading a file

"""f = open("demo.txt","r")
data=f.read(6)   #onlt reads first six letters but if () then reads the whole thing
print(data)

f.close()"""

"""f=open("demo.txt","r")     #ek bar pora data read hojaye ga to read line empty space dega
line1=f.readline()
print(line1)"""


#Writing to a file

"""f=open("demo.txt","w")        #Old data deletes and new appears
f.write("I want to learn wed development.")"""

"""f=open("demo.txt","a")
f.write("\nI am a software engineer.") """  #Adds data in previous


#If we enter a file name in w or a that doesn't exist then python iteself creates a new file


"""f=open("sample.txt","w")
f.write("Hello world.\nThis is me learning python.")

#Can also creat like this

f=open("sample.txt","a")
f.close()"""


"""f=open("demo.txt","r+")   #Can use this if we want to add something from the start in a file
f.write("abc")                #Pointer starting mein hota. we can also read
f.close()"""


"""f=open("demo.txt","w+")       #Can use this if we want to add something but previous data is wiped out
f.write("hehe")                #(truncate)      #can also read
f.close()"""


"""f=open("demo.txt","a+")
f.write("")        #nothing happens
f.write("abc")     #print abc at the end without truncating    #read and append        
f.close() """          #pointer at the end



#With Syntax  (Simplified way of writing above operations)

"""with open("demo.txt","r") as f:
    data=f.read()
    print(data)   """ #close file karna imp nhi when using with woh khudhi kardeta


#Deleting a file

"""import os    #pre installed module
os.remove("sample.txt")"""


#PRACTICE

"""f=open("practice.txt","w")
f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
f.close()"""

#WAF that replaces all occurences of java with python

"""with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    data=f.write(new_data)"""


#Search if the word "learning" exists in the file or not

"""with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("learning")):
        print("learning exists")
    else:
        print("learning do not exist")"""


#WAF to find in which line of the file does the word learning occur first.print -1 if not found

"""def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1
check_for_line()"""




"""with open("practice.txt","w") as f:
    data="Hi Everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java."
    f.write(data)"""

"""with open("practice.txt") as f:
    data=f.read()

new=data.replace("Java","Python")
print(new)

with open("practice.txt","w") as f:
    f.write(new)"""


"""with open("practice.txt") as f:
    data=f.read()

if "learning" in data:
    print("yes")
else:
    print("no")"""



"""def first():
    lineno=1
    with open("practice.txt","r") as f:
            while True: 
               data=f.readline()
               if "learning" in data:
                  print(lineno)
                  return
               lineno+=1
            
    return -1
first()"""

"""l=['a','b','c','d','e']

for i in l:
    for j in range(len(l)):
        print(" "*(j-1),end="")
        print(i,end="")
    print()"""



rows=6

for i in range(1,7):
    print(" "*(rows-i)+chr(63+i)*(i-1))




        



















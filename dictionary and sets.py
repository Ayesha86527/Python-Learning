"""info={
    "Name":"Ayesha",
    "Marks":93,
    "Field":"Software Engineering",
    "languages":["Python","Java","C"],
    "Interests":("CyberSecurity","DataScience","AI"),
    56.9:57
}
print(info)
print(info["Name"])

info["Name"]="Fateh Ramzal"
info["Surname"]="Wan Fateh"
print(info)

null_dict={}
null_dict["name"]="Ayesha"
print(null_dict)"""

#Nested Dictionaries

"""StudentInfo={
    "Name":"Ayesha",
    "Score":{
        "Maths":99,
        "Chemistry":95,
        "Physics":94
    }
}
print(StudentInfo)
print(StudentInfo["Score"])
print(StudentInfo["Score"]["Maths"])""" #99 

#Dictionary Methods

dict={
    "name":"Ayesha",
    "age":18,
    "Occupation":"Student"
}
#Key Method

print(dict.keys())
print(list(dict.keys()))   #To convert into list

"""print(len(dict))       #To find total no of keys
print(len(list(dict.keys()))) 

#Value Method

print(dict.values())
print(list(dict.values()))"""

#Item Method

"""print(dict.items())
print(list(dict.items()))
pairs=list(dict.items())
print(pairs[0]) """  #name:Ayesha

#get method

#print(dict["name2"])  #error
#print(dict.get("name2")) #None

#Update Method

"""dict.update({"City":"Karachi"})
print(dict)""" 

"""new_dict={"City":"Karachi"}
dict.update(new_dict)     #Is tareeqe se bhi karsakte 
print(dict) """        


#SETS

"""collection={1,2,3,4}
print(type(collection))

set={6,6,8,9,0}   #Set ignores duplicate values
print(set)
print(len(set)) """   #Total number of items

"""collection={} #Empty Dictionary
set_=set()    #Empty set
print(type(set_))"""

#Set Methods

#Add Method

"""set={1,2,3,4,5}
set.add(6)
print(set)"""

#Remove Method

"""set={1,2,3}
set.remove(3)
print(set)"""

#Clear Method

"""set={1,2,3} 
set.clear()
print(set)"""

#Pop Method

"""set={1,2,3}
set.pop()   #removes random value from set
print(set)"""

#Union Method

"""set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))"""

#Intersection Method

#print(set1.intersection(set2))




    










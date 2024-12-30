#Practice 5

#Store the following word meanings in a dictionary: table:a piece of furniture,list of facts and figures,cat:a small animal,

"""dict={
    "table":["a piece of furniture,list of facts and figures"],
    "cat":"a small animal"
}
print(dict)"""

#You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all students.
#python,java,c++,python,javascript,java,python,java,c++,c

"""ubjectlist={"python","java","c++","python","javascript","java","python","java","c++","c"}
classroomsneeded=len(subjectlist)
print(classroomsneeded)"""

#WAP to enter the marsks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and add one by one.
#Use the subject name as key and marks as value.

"""marks={}

x=int(input("enter maths marks:"))
marks.update({"maths":x})

x=int(input("enter phy marks: "))
marks.update({"phy":x})

x=int(input("enter chem marks:"))
marks.update({"chem":x})

print(marks)"""

#Figure out a way to store 9 and 9.0 as separate values in the set.

"""values={9,"9.0"}
print(values)

values={
    ("float",9.0),
    ("int",9)
}
print(values)"""




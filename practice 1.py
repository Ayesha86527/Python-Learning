#Write a program to input two numbers and print their sum

"""num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print("sum=",num1+num2)"""

#WAP to input side of a square

"""a=int(input("Enter side:"))
print("Area of square:",a**2)"""

#WAP to input 2 floating point numbers and print their average 

"""a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=a+b
print("average:",c/2)"""

#WAP to input 2 int numbers a and b.Print true if a is greater than b or equal to b.If not print false.

"""a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print(a>=b)"""

"""import textwrap

def wrap(string, max_width):
    wrapped_text=textwrap.wrap(string,max_width)
    return "\n".join(wrapped_text)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)"""

"""def print_formatted(number):
    
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)"""

n=int(input())

for i in range(1,n+1):
    octal=oct(i)
    print(octal[2:],end="")
    



for j in range(1,n+1):
    hexa=hex(j)
    print(hexa[2:],end="")



for k in range(1,n+1):
    binary=bin(k)
    print(binary[2:],end="")

    










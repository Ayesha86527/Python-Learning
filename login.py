from tkinter import *
from tkinter import messagebox
m=Tk()
m.title("Shopify.com Login")
var1=StringVar
var2=StringVar
def login():
        try:
           messagebox.showinfo("Login Update","You have logged in successfully!")
        except:
            print("Enter the correct password and username!")

def submit():
    try:
       messagebox.showinfo("Account Created","Welcome to Shopify.com!")
    except:
        print("Please enter all details!")

def signup():
    var3=StringVar
    var4=StringVar
    var5=StringVar
    var6=StringVar
    win=Toplevel(m)
    win.title("Sign in")
    win.geometry("400x400")
    win.configure(bg='#F4C2C2')
    lab2=Label(win,text="First Name",bg='#F4C2C2',fg='black').pack(pady=20)
    en1=Entry(win,textvariable=var3).pack(pady=5)
    lab3=Label(win,text="Last Name",bg='#F4C2C2',fg='black').pack(pady=10)
    en2=Entry(win,textvariable=var4).pack(pady=5)
    lab4=Label(win,text="Date Of Birth",bg='#F4C2C2',fg='black').pack(pady=10)
    en3=Entry(win,textvariable=var5).pack(pady=5)
    lab5=Label(win,text="Email or Phone",bg='#F4C2C2',fg='black').pack(pady=10)
    en4=Entry(win,textvariable=var6).pack(pady=5)
    b3=Button(win,text="Submit",command=submit).pack(pady=10)
    
m.geometry("800x600")
m.configure(bg='#577899')
l1=Label(m,text="Shopify.com",fg='#577899',bg="gold",font=('Times New Roman',40,'bold'))
l1.pack(side=TOP,fill=X)
l2=Label(m,text="Login to Continue Shopping!",bg='#577899',fg='black',font=('Times New Roman',30,'bold'))
l2.pack(pady=10)
l3=Label(m,text="Email or Phone",fg='white',bg='#577899',font=('Times New Roman',16))
l3.pack(pady=10)
e1=Entry(m,textvariable=var1).pack()
l3=Label(m,text="Password",fg='white',bg='#577899',font=('Times New Roman',16))
l3.pack(pady=10)
e2=Entry(m,textvariable=var2).pack()
b1=Button(m,text="Login",bg='#F4C2C2',fg='black',width=12,command=login).pack(pady=5)
l4=Label(m,text="Don't have an account?",bg='#577899',fg='black',font=('Times New Roman',12))
l4.pack(pady=10)
b2=Button(m,text="Sign Up",bg='#F4C2C2',fg='black',width=12,command=signup).pack()

m.mainloop()
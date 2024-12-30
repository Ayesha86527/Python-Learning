#calculator window with buttons

from tkinter import *

"""cal=Tk()
cal.geometry("545x250")
cal.minsize(200,100)
cal.maxsize(690,590)

cal.configure(bg='#FFA500')

f1=Frame(cal,borderwidth=8,relief=SUNKEN)
f1.grid()

l1=Label(cal,text="MY CALCULATOR",bg="green",fg="white",width=20,relief=SUNKEN,font="comicsans 16")
l1.grid(row=0,column=0)

e1=Entry(cal,bg='white')
e1.grid(row=1,column=0,pady=20,padx=30)

b1=Button(e1,text="C",bg="black",fg="white",width=10)
b1.grid(row=2,column=0)

b2=Button(e1,text="/",bg="black",fg="white",width=10)
b2.grid(row=2,column=1)

b3=Button(e1,text="x",bg="black",fg="white",width=10)
b3.grid(row=2,column=2)

b4=Button(e1,text="<x>",bg="black",fg="white",width=10)
b4.grid(row=2,column=3)

b5=Button(e1,text="7",bg="black",fg="white",width=10)
b5.grid(row=3,column=0)

b6=Button(e1,text="8",bg="black",fg="white",width=10)
b6.grid(row=3,column=1)

b7=Button(e1,text="9",bg="black",fg="white",width=10)
b7.grid(row=3,column=2)

b8=Button(e1,text="-",bg="black",fg="white",width=10)
b8.grid(row=3,column=3)

b9=Button(e1,text="4",bg="black",fg="white",width=10)
b9.grid(row=4,column=0)

b10=Button(e1,text="5",bg="black",fg="white",width=10)
b10.grid(row=4,column=1)

b11=Button(e1,text="6",bg="black",fg="white",width=10)
b11.grid(row=4,column=2)

b12=Button(e1,text="+",bg="black",fg="white",width=10)
b12.grid(row=4,column=3)

b13=Button(e1,text="1",bg="black",fg="white",width=10)
b13.grid(row=5,column=0)

b14=Button(e1,text="2",bg="black",fg="white",width=10)
b14.grid(row=5,column=1)

b15=Button(e1,text="3",bg="black",fg="white",width=10)
b15.grid(row=5,column=2)

b13=Button(e1,text="=",bg="green",fg="white",width=10)
b13.grid(row=5,column=3)

b14=Button(e1,text="%",bg="black",fg="white",width=10)
b14.grid(row=6,column=0)

b15=Button(e1,text="0",bg="black",fg="white",width=10)
b15.grid(row=6,column=1)

b16=Button(e1,text=".",bg="black",fg="white",width=10)
b16.grid(row=6,column=2)

b17=Button(e1,text="Ans",bg="green",fg="white",width=10)
b17.grid(row=6,column=3)

b18=Button(e1,text="!",bg="black",fg="white",width=10)
b18.grid(row=7,column=0)

b19=Button(e1,text="^2",bg="black",fg="white",width=10)
b19.grid(row=7,column=1)

b20=Button(e1,text="^3",bg="black",fg="white",width=10)
b20.grid(row=7,column=2)

b21=Button(e1,text="log",bg="black",fg="white",width=10)
b21.grid(row=7,column=3)



cal.mainloop()"""


"""from tkinter import *

root=Tk()

root.geometry("655x333")

f1=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)

f1.pack(side=LEFT,fill="y")


f2=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Pycharm")
l.pack(pady=142)


l=Label(f2,text="Welcome to sublime text",font="Helvetica 16 bold")
l.pack()

root.mainloop()"""

#buttons ek sath with border
"""from tkinter import *

root=Tk()

root.geometry("655x333")

def hello():
    print("Hello")

def okay():
    print("Okay")

f=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
f.pack(side=LEFT,anchor="nw")

b1=Button(f,fg="black",text="Print",command=hello)
b1.pack(side=LEFT)

b2=Button(f,fg="black",text="Print",command=okay)
b2.pack(side=LEFT)

b3=Button(f,fg="black",text="Print")
b3.pack(side=LEFT)

b4=Button(f,fg="black",text="Print")
b4.pack(side=LEFT)

root.mainloop()"""

"""from tkinter import *

root=Tk()

root.geometry("655x333")

user=Label(root,text="Username")
password=Label(root,text="Password")
user.grid()
password.grid()

#variable classes in tkinter 
#boolean_var,double_var,int_var,string_var

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

def getval():
    print(uservalue.get())
    print(passvalue.get())

Button(text="Submit",command=getval).grid()

root.mainloop()"""

#TRAVEL FORM
"""from tkinter import *

root=Tk()

def getvar():
    print("Submitted form")
    print(f"{namevar.get(),phonevar.get(),emailvar.get(),payvar.get()}")
    with open("records.txt","a") as f:
        f.write(f"{namevar.get(),phonevar.get(),emailvar.get(),payvar.get()}")

root.geometry("645x468")

Label(root,text="WELCOME TO ARKAYS TRAVELS",font="comicsansms 13 bold").grid(row=0,column=3,pady=15,padx=50)
#text for form
name=Label(root,text="Name")
email=Label(root,text="Email")
phone=Label(root,text="Phone")
pay=Label(text="Payment Mode")
#pack text for form
name.grid(row=1,column=2)
email.grid(row=2,column=2)
phone.grid(row=3,column=2)
pay.grid(row=4,column=2)
#kinter var for storing entry
namevar=StringVar()
phonevar=StringVar()
emailvar=StringVar()
payvar=StringVar()
foodvar=IntVar()
#entry for form
name_entry=Entry(root,textvariable=namevar)
email_entry=Entry(root,textvariable=emailvar)
phone_entry=Entry(root,textvariable=phonevar)
payment_entry=Entry(root,textvariable=payvar)

#pack entry
name_entry.grid(row=1,column=3)
email_entry.grid(row=2,column=3)
phone_entry.grid(row=3,column=3)
payment_entry.grid(row=4,column=3)

#checkbox

food=Checkbutton(text="Want to pre-book your meals?",variable=foodvar)
food.grid(row=6,column=3)

#button and packing it and assigning it a command

Button(text="Submit your form",command=getvar).grid(row=7,column=3)



root.mainloop()"""

"""from tkinter import *

root=Tk()
root.title("GUI")

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")

can_wid=Canvas(root,width=canvas_width,height=canvas_height)

can_wid.pack()
#line goes from point x1,y1 to x2,y2
can_wid.create_line(1,200,800,0)

can_wid.create_rectangle(2,6,500,900,fill="purple")

can_wid.create_text(200,200,text="HARRYYY")

root.mainloop()"""

"""from tkinter import *


root=Tk()

def hello(event):
    print(f"Hello {event.x},{event.y}")

root.title("EVENT")
root.geometry("644x489")

wid=Button(root,text="Click")
wid.pack()

wid.bind('<Button-1>',hello)

root.mainloop()"""


#WINDOW RESIZER
"""from tkinter import *
root=Tk()

def change():
    w=width.get()
    h=height.get()
    root.geometry(f"{w}x{h}")
    



root.geometry("566x345")

root.title("WINDOW RESIZER")

w=Label(text="Enter the width:").grid(row=1,column=0)
h=Label(text="Enter the height:").grid(row=2,column=0)
width=IntVar()
height=IntVar()

w_entry=Entry(root,textvariable=width).grid(row=1,column=1)
h_entry=Entry(root,textvariable=height).grid(row=2,column=1)

b=Button(root,text="Change",command=change).grid(row=3,column=1,pady=20)

root.mainloop()"""

#menu and submenu

"""from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()

def msg():
    tmsg.showinfo("Help","We are here to help!")

def rate():
    value=tmsg.askquestion("Was your experience?", "Was your experience Good?")
    print(value)
    if value=="yes":
        msg="Great!"
    else:
        msg="Tell us what went wrong?"
    tmsg.showinfo(msg)

def move():
    ans=tmsg.askretrycancel("move","stay")
    if ans:
        print("move")
    else:
        print("Stay")



root.geometry("645x446")
root.title("PyCharm")

#USE THESE TO CREATE NON DROP DOWN MENU
menu=Menu(root)
menu.add_command(label="File")
menu.add_command(label="Exit",command=quit)
root.config(menu=menu)

my=Menu(root)

m1=Menu(my,tearoff=0)

m1.add_command(label="Save")
m1.add_command(label="Save As")
m1.add_separator()
m1.add_command(label="Open")
m1.add_command(label="Print")

my.add_cascade(label="File",menu=m1)

root.config(menu=my)

m2=Menu(my,tearoff=0)
m2.add_command(label="Crop")
m2.add_command(label="Max")
m2.add_command(label="Min")

my.add_cascade(label="Edit",menu=m2)

m3=Menu(my,tearoff=0)
m3.add_command(label="Click for help",command=msg)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="Move",command=move)
my.add_cascade(label="Help",menu=m3)
root.config(menu=my)



root.config(menu=my)

root.mainloop()"""

"""from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()

def get_dol():
    print(f"We have credited {hor_slider.get()} dollars to your bank account.")
    tmsg.showinfo("Amount Credited",f"We have credited {hor_slider.get()} dollars to your bank account.")


root.geometry("678x456")

root.title("GUI")

#slider=Scale(root,from_=0,to=444).pack()   #vertical slider

Label(root,text="How many dollars do you want?").pack()

hor_slider=Scale(root,from_=0,to=456,orient=HORIZONTAL,tickinterval=300)
hor_slider.set(201)

Button(root,text="Get dollars!",command=get_dol).pack()

hor_slider.pack()

root.mainloop()"""


#restraunt rating

"""from tkinter import *
import tkinter.messagebox as tmsg


root=Tk()

def rate():
    with open("rate.txt","a") as f:
        f.write(f"{slider.get()}\n")


root.geometry("678x482")

root.title("Our Rating Page")

Label(root,text="Rate your experience at our restraunt:)",font="Arial 16").pack()

slider=Scale(root,from_=1,to=10,orient=HORIZONTAL,tickinterval=4)

slider.pack()

Button(root,text="Submit",command=rate).pack()

root.mainloop()"""

#LOGIN WINDOW 


"""from tkinter import *

root=Tk()

root.geometry("678x478")

root.title("Login In")

root.configure(bg='#585994')  #lavendar

Label(root,text="Login",fg='#F4C2C2',bg='#585994',font="Arial 25 bold").grid(row=1,column=10,padx=50,pady=20)

Label(root,text="Username",bg='#585994',fg="white").grid(row=5,column=5,padx=50,pady=5)

Entry(root).grid(row=5,column=6)

Label(root,text="Password",bg='#585994',fg="white").grid(row=6,column=5,padx=50,pady=5)

Entry(root).grid(row=6,column=6)

Button(root,text="Log in",bg='#F4C2C2').grid(row=9,column=6,pady=20)





root.mainloop()"""



"""from tkinter import *

import pyshorteners"""








"""win=Tk()

def short():
    shortener=pyshorteners.Shortener()
    short_url=shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0,short_url))


win.geometry("678x487")

win.title("URL Shortener")

Label(win,text="Enter the URL:").pack(pady=30)

longurl_entry=Entry(win).pack(pady=5)

Label(win,text="Shortened URL:").pack(pady=10)

shorturl_entry=Entry(win).pack(pady=5)

Button(win,text="Shorten URL",command=short).pack(pady=10)

win.mainloop()"""


#adding icon/images


"""from tkinter import *

from PIL import ImageTk,Image

root=Tk()

root.title("Icon")

root.geometry("678x456")

root.iconbitmap("C:/Users/AAC/Documents/thermometer_temperature_medical_measurement_fever_icon_264387.webp")

my_img=ImageTk.PhotoImage(Image.open("C:/Users/AAC/Documents/—Pngtree—pink watercolor brushes_5054156.png"))

l=Label(image=my_img)
l.pack()

button_quit=Button(root,text="Exit",command=root.quit).pack()

root.mainloop()"""
































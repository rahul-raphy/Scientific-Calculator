from tkinter import * 
import tkinter.messagebox as tmsg
import math as m

root = Tk()

root.minsize(520,340)
root.maxsize(520,340)

root.title("SCIENTIFIC CALCULATOR")
root.wm_iconbitmap("calculator.ico")


sc = StringVar()
sc = Entry(root,width=31,textvariable=sc,relief=SUNKEN,font="cosmicsansms 20")
sc.grid(row=0,column=0,columnspan=10,padx=11,pady=12) 

def abt():
    abt = "Developed by Rahul Raphy \nTechwingsys, Kochi" 
    tmsg.showinfo("About",abt)

mainmenu = Menu(root)

submenu = Menu(mainmenu,tearoff=0)

mainmenu.add_command(label="About",command=abt) 
mainmenu.add_command(label="Exit",command=quit)

root.config(menu=mainmenu)

def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.delete(0,END)
    if text=="sin":
        sc.insert(0,m.sin(float(val)))
    elif text=="cos":
        sc.insert(0,m.cos(float(val)))  
    elif text=="tan":
        sc.insert(0,m.tan(float(val)))
    elif text=="log":
        if(float(val)<=0.00):
            sc.insert(0,"Not Possible")
        else:
            sc.insert(0,m.log10(float(val)))
    elif text=="ln":
        if(float(val)<=0.00):
            sc.insert(0,"Not Possible")
        else:
            sc.insert(0,m.log(float(val)))
    elif text=="√":
        sc.insert(0,m.sqrt(float(val)))
    elif text=="!":
        sc.insert(0,m.factorial(int(val)))
    elif text=="rad":
        sc.insert(0,m.radians(float(val)))
    elif text=="deg":
        sc.insert(0,m.degrees(float(val)))
    elif text=="1/x":
        if(val=="0"):
            sc.insert(0,"ꝏ")
        else:
            sc.insert(0,1/float(val))
    elif text=="π":
        if val=="":
             ans = str(m.pi)
             sc.insert(0,ans)
        else:
            ans = str(float(val) * (m.pi))
            sc.insert(0,ans)
    elif text=="e":
        if val=="":
            sc.insert(0,str(m.e))
        else:
            sc.insert(0, str(float(val) * (m.e)))
    

def click(event):
    key = event.widget
    text = key['text']
    oldValue = sc.get()
    sc.delete(0,END)
    newValue = oldValue + text
    sc.insert(0,newValue)
              

def clr(event):
    sc.delete(0,END)
    

def backspace(event):
    entered = sc.get()
    length = len(entered)-1
    sc.delete(length,END)
    

def calculate(event):
    answer = sc.get()
    if "^" in answer:
        answer = answer.replace("^","**")
    answer = eval(answer)
    sc.delete(0,END)
    sc.insert(0,answer)
    
    
class Calculator:
    def __init__(self,txt,r,c,funcName,color="white"):
        self.var = Button(root,text=txt,padx=3,pady=5,fg="black",bg=color,width=10,font="cosmicsansms 12")
        self.var.bind("<Button-1>",funcName)
        self.var.grid(row=r,column=c)


btn0 = Calculator("sin",1,0,sciCal)

btn1 = Calculator("cos",1,1,sciCal)

btn2 = Calculator("tan",1,2,sciCal)

btn3 = Calculator("log",1,3,sciCal)

btn4 = Calculator("ln",1,4,sciCal)

btn5 = Calculator("(",2,0,click)

btn6 = Calculator(")",2,1,click)

btn7 = Calculator("^",2,2,click)

btn8 = Calculator("√",2,3,sciCal)

btn9 = Calculator("!",2,4,sciCal)

btn10 = Calculator("π",3,0,sciCal)

btn11 = Calculator("1/x",3,1,sciCal)

btn12 = Calculator("deg",3,2,sciCal)

btn13 = Calculator("rad",3,3,sciCal)

btn14 = Calculator("e",3,4,sciCal)

btn15 = Calculator("9",4,0,click)

btn16 = Calculator("8",4,1,click)

btn17 = Calculator("7",4,2,click)

btn18 = Calculator("+",4,3,click)

btn19 = Calculator("/",4,4,click)

btn20 = Calculator("6",5,0,click)

btn21 = Calculator("5",5,1,click)

btn22 = Calculator("4",5,2,click)

btn23 = Calculator("-",5,3,click)

btn24 = Calculator("*",5,4,click)

btn25 = Calculator("3",6,0,click)

btn26 = Calculator("2",6,1,click)

btn27 = Calculator("1",6,2,click)

btn28 = Calculator("00",6,3,click)

btn29 = Calculator("%",6,4,click)

btn30 = Calculator("C",7,0,clr,"red")

btn31 = Calculator("⌦",7,1,backspace,"gold")

btn32 = Calculator("0",7,2,click)

btn33 = Calculator(".",7,3,click)

btn34 = Calculator("=",7,4,calculate,"light green")

root.mainloop()

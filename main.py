from tkinter import *
root=Tk()
root.title("calculator")
e=Entry(root,width=35)
e.grid(row=0,column=0,columnspan=4)

def button_click(number):
  current=e.get()
  e.delete(0,END)
  e.insert(0,str(current)+str(number))
  

def button_add():
  global first_number
  global math
  math="add"
  first_number=e.get()
  e.delete(0,END)

def button_clear():
  e.delete(0,END)

def button_equal():
  second_number=e.get()
  e.delete(0,END)
  if math=="add":
    e.insert(0,int(first_number)+int(second_number)) 
  if math=="sub":
    e.insert(0,int(first_number)-int(second_number))  
  if math=="mul":
    e.insert(0,int(first_number)*int(second_number))
  if math=="div":
    e.insert(0,int(first_number)/int(second_number))

def button_sub():
  global first_number
  global math
  math="sub"
  first_number=e.get()
  e.delete(0,END)
  
def button_mul():
  global first_number
  global math
  math="mul"
  first_number=e.get()
  e.delete(0,END)
  
def button_div():
  global first_number
  global math
  math="div"
  first_number=e.get()
  e.delete(0,END)
  
  


button1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))

buttonadd=Button(root,text="+",padx=79,pady=20,command=button_add)
buttonsub=Button(root,text="-",padx=40,pady=20,command=button_sub)
buttonmul=Button(root,text="*",padx=40,pady=20,command=button_mul)
buttondiv=Button(root,text="/",padx=40,pady=20,command=button_div)
buttonequal=Button(root,text="=",padx=91,pady=20,command=button_equal)


buttonclear=Button(root,text="clear",padx=61,pady=20,command=button_clear)


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)


button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)


button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4,column=0)
buttonadd.grid(row=4,column=1,columnspan=2)
buttonequal.grid(row=5,column=0,columnspan=2)
buttonclear.grid(row=5,column=1,columnspan=2)

buttonsub.grid(row=6,column=0)
buttonmul.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)


root.mainloop()
from tkinter import *
root=Tk()
root.title("Calculator")

#creating an entry box
input=Entry(root,width=39,borderwidth=5)
input.grid(row=0,column=0,columnspan=5,padx=5,pady=5)

def clearall():   #function to clear everything
    input.delete(0,END)

def delete(): #function to delete the last character
    input.delete(input.index("end")-1)
i=0
def on_click(value):  #function to enter pressed button
    global i
    input.insert(i,value)
    i+=1

def calc():  #function to calculate the expression
    exp=input.get()
    try:

        result=eval(exp)
        clearall()
        input.insert(0,result)
    except:
        clearall()
        input.insert(0,"error")

#creating buttons

btn_ac=Button(root,text="AC",padx=10,pady=20,command=clearall).grid(row=1,column=0)
btn_del=Button(root,text="DEL",padx=10,pady=20,command=delete).grid(row=1,column=1)
btn_div=Button(root,text="/",padx=20,pady=20,command=lambda:on_click("/")).grid(row=1,column=2)
btn_mul=Button(root,text="x",padx=20,pady=20,command=lambda:on_click("*")).grid(row=1,column=3)

btn_7=Button(root,text="7",padx=20,pady=20,command=lambda:on_click("7")).grid(row=2,column=0)
btn_8=Button(root,text="8",padx=20,pady=20,command=lambda:on_click("8")).grid(row=2,column=1)
btn_9=Button(root,text="9",padx=20,pady=20,command=lambda:on_click("9")).grid(row=2,column=2)
btn_sub=Button(root,text="-",padx=20,pady=20,command=lambda:on_click("-")).grid(row=2,column=3)

btn_4=Button(root,text="4",padx=20,pady=20,command=lambda:on_click("4")).grid(row=3,column=0)
btn_5=Button(root,text="5",padx=20,pady=20,command=lambda:on_click("5")).grid(row=3,column=1)
btn_6=Button(root,text="6",padx=20,pady=20,command=lambda:on_click("6")).grid(row=3,column=2)
btn_add=Button(root,text="+",padx=20,pady=20,command=lambda:on_click("+")).grid(row=3,column=3)

btn_1=Button(root,text="1",padx=20,pady=20,command=lambda:on_click("1")).grid(row=4,column=0)
btn_2=Button(root,text="2",padx=20,pady=20,command=lambda:on_click("2")).grid(row=4,column=1)
btn_3=Button(root,text="3",padx=20,pady=20,command=lambda:on_click("3")).grid(row=4,column=2)
btn_equal=Button(root,text="=",padx=20,pady=50,command=calc).grid(row=4,column=3,rowspan=2)

btn_0=Button(root,text="0",padx=50,pady=20,command=lambda:on_click("0")).grid(row=5,column=0,columnspan=2)
btn_dec=Button(root,text=".",padx=20,pady=20,command=lambda:on_click(".")).grid(row=5,column=2)


root.resizable(False,False)
root.mainloop()

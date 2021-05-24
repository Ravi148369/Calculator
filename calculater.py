from tkinter import *
root=Tk()
root.geometry("500x850")
root.title("Hello World")
# root.configure(background="grey")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill="x",pady=15,padx=15)

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(f"text {text}")
    if text=="=":
        try:
            value=eval(screen.get())
        except Exception as e:
            scvalue.set("ERROR")
            scree.update()
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

#frame 1 
f=Frame(root,bg="grey")

b=Button(f,text="9",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="8",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="7",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()

#frame 2
f=Frame(root,bg="grey")

b=Button(f,text="6",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="5",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="4",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()

#frame 3
f=Frame(root,bg="grey")

b=Button(f,text="3",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="2",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="1",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()

#frame 4
f=Frame(root,bg="grey")

b=Button(f,text="0",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="-",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="*",font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()


#frame 5
f=Frame(root,bg="grey")

b=Button(f,text="/",font="lucida 35 bold")
b.pack(side=LEFT,padx=14,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="%",font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="=",font="lucida 35 bold")
b.pack(side=LEFT,padx=14,pady=12)
b.bind("<Button-1>",click)

f.pack()

#frame 6
f=Frame(root,bg="grey")

b=Button(f,text="C",font="lucida 35 bold")
b.pack(padx=15,pady=12)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()
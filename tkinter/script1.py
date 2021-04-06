from tkinter import * 


window=Tk()

def km_to_miles():
    #use get funti to get string value
    print(e1_value.get())
    miles=float(e1_value.get())*1.6
    #we must insert text in ti with insert()
    #END to put text at the end of widget
    t1.insert(END,miles)
# use command to execute function on button execute
#don't put brackets on func here!
b1=Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)
#b1.pack()

#now entry widget
#use textvariable to declare value
#declare here
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
#now text widget
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()

import tkinter as tk
root = tk.Tk()
calci=''
root.geometry("350x380")
root.resizable(False,False)
root.title('Calculator')


textbox= tk.Text(root,height=3,font=('Arial',16))
textbox.pack(padx=10,pady=10)

buttonframe = tk.Frame(root)#gives config of grid which used for fill
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

def add(n):
    global calci
    calci=calci+str(n)
    textbox.delete(1.0,"end")
    textbox.insert(1.0,calci)

def clear():
    global calci
    textbox.delete(1.0,"end")

def exit():
    root.destroy()
def evaluation():
    global calci
    try:
        result=str(eval(calci))
        calci=""
        textbox.delete(1.0,"end")
        textbox.insert(1.0,result)
    except:
        clear()
        textbox.insert(1.0,'Error')
        


btn1 = tk.Button(buttonframe,text='1', font=('Arial',18),command=lambda: add(1))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)#used for expand throughtout the window

btn2 = tk.Button(buttonframe,text='2', font=('Arial',18),command=lambda:add(2))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe,text='3', font=('Arial',18),command=lambda:add(3))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe,text='4', font=('Arial',18),command=lambda:add(4))
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe,text='5', font=('Arial',18),command=lambda:add(5))
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe,text='6',font=('Arial',18),command=lambda:add(6))
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe,text='7',font=('Arial',18),command=lambda:add(7))
btn7.grid(row=2,column=0,sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe,text='8',font=('Arial',18),command=lambda:add(8))
btn8.grid(row=2,column=1,sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe,text='9',font=('Arial',18),command=lambda:add(9))
btn9.grid(row=2,column=2,sticky=tk.W+tk.E)

btn0 = tk.Button(buttonframe,text='0',font=('Arial',18),command=lambda:add(0))
btn0.grid(row=3,column=1,sticky=tk.W+tk.E)


btn_plus = tk.Button(buttonframe,text='+', font=('Arial',18),command=lambda:add('+'))
btn_plus.grid(row=0,column=3,sticky=tk.W+tk.E)

btn_minus= tk.Button(buttonframe,text='-', font=('Arial',18),command=lambda:add('-'))
btn_minus.grid(row=1,column=3,sticky=tk.W+tk.E)



btn_multilply= tk.Button(buttonframe,text='*', font=('Arial',18),command=lambda:add('*'))
btn_multilply.grid(row=2,column=3,sticky=tk.W+tk.E)


btn_minus= tk.Button(buttonframe,text='-', font=('Arial',18),command=lambda:add('-'))
btn_minus.grid(row=1,column=3,sticky=tk.W+tk.E)

btn_obracket = tk.Button(buttonframe,text='(',font=('Arial',18),command=lambda:add('('))
btn_obracket.grid(row=3,column=0,sticky=tk.W+tk.E)

btn_cbracket = tk.Button(buttonframe,text=')',font=('Arial',18),command=lambda:add(')'))
btn_cbracket.grid(row=3,column=2,sticky=tk.W+tk.E)

btn_div= tk.Button(buttonframe,text='/', font=('Arial',18),command=lambda:add('/'))
btn_div.grid(row=3,column=3,sticky=tk.W+tk.E)

btn_c= tk.Button(buttonframe,text='C', font=('Arial',18),command=lambda:clear())
btn_c.grid(row=4,column=0,columnspan=2,sticky=tk.W+tk.E)

btn_equal= tk.Button(buttonframe,text='=', font=('Arial',18),command=lambda:evaluation())
btn_equal.grid(row=4,column=2,columnspan=2,sticky=tk.W+tk.E)

btn_exit= tk.Button(buttonframe,text='EXIT', font=('Arial',18),command=lambda:exit())
btn_exit.grid(row=5,column=1,columnspan=2)


buttonframe.pack(fill='x')



root.mainloop()








import tkinter
from tkinter import *
from tkinter.messagebox import *
import math
a = Tk()
a.title("Kalkulator")
s1 = ''
def dc(ca=''):
    if ca == '=':
        try:
            b = eval(f.get())
            f.delete(0, END)
            f.insert(END, b)
        except:
            showerror('Ошибка ввода', 'Возникла ошибка ввода')

    else:
        current = f.get()
        print(current)
        f.delete(0, END)
        f.insert(END, current + ca)

f = Entry(a,width = 30 , font=('Arial', 20))
f.grid(row=0, column=0, columnspan=4)

b1 = Button(a, text='1', width=30, pady = 10 , command = lambda t='1':dc(t))
b1.grid(row=1, column=0)


b2 = Button(a, text='2', width=30, pady = 10,  command = lambda t='2':dc(t))
b2.grid(row=1, column=1)

b3 = Button(a, text='3', width=30, pady = 10, command = lambda t='3':dc(t))
b3.grid(row=1, column=2)

b4 = Button(a, text='+', width=30 , pady = 10, command = lambda t='+':dc(t))
b4.grid(row=1, column=3)

a1 = Button(a, text='4', width=30, pady = 10, command = lambda t='4':dc(t))
a1.grid(row=2, column=0)

a2 = Button(a, text='5', width=30, pady = 10, command = lambda t='5':dc(t))
a2.grid(row=2, column=1)

a3 = Button(a, text='6', width=30, pady = 10, command = lambda t='6':dc(t))
a3.grid(row=2, column=2)

a4 = Button(a, text='-', width=30 , pady = 10, command = lambda t='-':dc(t))
a4.grid(row=2, column=3)

c1 = Button(a, text='7', width=30, pady = 10, command = lambda t='7':dc(t))
c1.grid(row=3, column=0)

c2 = Button(a, text='8', width=30, pady = 10, command = lambda t='8':dc(t))
c2.grid(row=3, column=1)

c3 = Button(a, text='9', width=30, pady = 10, command = lambda t='9':dc(t))
c3.grid(row=3, column=2)

c4 = Button(a, text='=', width=30 , pady = 10, command = lambda t='=':dc(t))
c4.grid(row=3, column=3)


c5 = Button(a, text='.', width=30, pady = 10, command = lambda t='.':dc(t))
c5.grid(row=4, column=0)

c6 = Button(a, text='0', width=30, pady = 10, command = lambda t='0':dc(t))
c6.grid(row=4, column=1)

c7 = Button(a, text='*', width=30 , pady = 10, command = lambda t='*':dc(t))
c7.grid(row=4, column=2)
b1 = 1
b2 = 2
b3 = 3
b4 = "+"
a1 =4
a2 =5
a3=6
a4="-"
c1=7
c2=8
c3=9
c4="="








a.mainloop()




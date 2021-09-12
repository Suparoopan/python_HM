from tkinter import *
 
expression = ""
 
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
def equalpress():
    try:
 
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
 
    except:
 
        equation.set(" error ")
        expression = ""

def backspace():
    global expression
    expression = e.get()
    lenght = len(expression)-1
    e.delete(lenght)
 
def clear():
    global expression
    expression = ""
    equation.set("")
 
if __name__ == "__main__":
    
    gui = Tk()
 
    gui.configure(background="black")
 
    gui.title("Calculator")
 
    gui.geometry("500x300")
 
    equation = StringVar()
 
    expression_field = Entry(gui, textvariable=equation,justify='right'
          , bd=20, bg="#C0C0C0",font='bold')
    expression_field.grid(columnspan=10,rowspan=3, ipadx=100)

    back=Button(gui,text="<-",width=5,command=lambda:backspace('<-'))
    back.grid(row=7,column=2)
    
    
    button1 = Button(gui, text=' 1 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(1), height=2, width=15)
    button1.grid(row=3, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(2), height=2, width=15)
    button2.grid(row=3, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(3), height=2, width=15)
    button3.grid(row=3, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(4), height=2, width=15)
    button4.grid(row=4, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(5), height=2, width=15)
    button5.grid(row=4, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(6), height=2, width=15)
    button6.grid(row=4, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(7), height=2, width=15)
    button7.grid(row=5, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(8), height=2, width=15)
    button8.grid(row=5, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(9), height=2, width=15)
    button9.grid(row=5, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='#C0C0C0',
                    command=lambda: press(0), height=2, width=15)
    button0.grid(row=6, column=1)
 
    plus = Button(gui, text=' + ', fg='black', bg='#FFFF00',
                command=lambda: press("+"), height=2, width=20)
    plus.grid(row=3, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='#FFFF00',
                command=lambda: press("-"), height=2, width=20)
    minus.grid(row=4, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='#FFFF00',
                    command=lambda: press("*"), height=2, width=20)
    multiply.grid(row=5, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='#FFFF00',
                    command=lambda: press("/"), height=2, width=20)
    divide.grid(row=6, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='red',
                command=equalpress, height=2, width=15)
    equal.grid(row=6, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red',
                command=clear, height=3, width=20)
    clear.grid(row=7, column=3)
 
    Decimal= Button(gui, text='.', fg='black', bg='#C0C0C0',
                    command=lambda: press('.'), height=2, width=15)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()

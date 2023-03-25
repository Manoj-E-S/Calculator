#!/usr/bin/python3

'''
Simple Calculator
'''

from tkinter import *

def numClick(char: str, textBox: Entry):
    textBox.insert(END, char)

def evaluate(textBox: Entry):
    text = textBox.get()
    textBox.delete(0, END)
    textBox.insert(0, eval(text))

def utilBtn(op: str, textBox: Entry):
    if op == 'BS':
        textBox.delete(len(textBox.get())-1, END)
    else:
        textBox.delete(0, END)

################################################################## Window ###############################################################

# Create Window
root = Tk()
root.title('Calculator')

# Textbox to input calculations
inputBox = Entry(root, bg="#ffffff", fg="#000000", width=35, border=5)
inputBox.grid(row=0, column=0, columnspan=5, rowspan=2)

# Buttons: Numpad
row, col = 2, 0
buttons = []
for i in range(1, 10):

    buttons.append(Button(root, text=str(i), padx=20, pady=20, bg="#ffffff", fg="#000000", command=lambda char = str(i): numClick(char, inputBox)))
    buttons[i-1].grid(row=row, column=col)
    
    row = row + 1 if col == 2 else row
    col = 0 if col == 2 else col + 1

buttons.append(Button(root, text=str(0), padx=49, pady=20, bg="#ffffff", fg="#000000", command=lambda: numClick(str(0), inputBox)))
buttons[9].grid(row=5, column=0, columnspan=2)

# Buttons: Operators
Add = Button(root, text='+', padx=20, pady=20, bg="#ffffff", fg="#000000", command=lambda: numClick('+', inputBox))
Sub = Button(root, text='-', padx=22, pady=20, bg="#ffffff", fg="#000000", command=lambda: numClick('-', inputBox))
Mul = Button(root, text='x', padx=20, pady=20, bg="#ffffff", fg="#000000", command=lambda: numClick('*', inputBox))
Div = Button(root, text='/', padx=22, pady=20, bg="#ffffff", fg="#000000", command=lambda: numClick('/', inputBox)) 
paro = Button(root, text='(', padx=20, pady=20, bg="#ffffff", fg="#000000", command=lambda: numClick('(', inputBox))
parc = Button(root, text=')', padx=20, pady=20, bg="#ffffff", fg="#000000", command=lambda: numClick(')', inputBox))
Eq = Button(root, text='=', padx=16, pady=50, bg="#95bb72", fg="#ffffff", command=lambda: evaluate(inputBox))

Add.grid(row=2, column=3)
Sub.grid(row=3, column=3)
Mul.grid(row=4, column=3)
Div.grid(row=5, column=3)
paro.grid(row=2, column=4)
parc.grid(row=3, column=4)
Eq.grid(row=4, column=4, rowspan=2)

# Utility Buttons 
decpt = Button(root, text='.', padx=22, pady=20, bg="#ffffff", fg="#000000", command=lambda: numClick('.', inputBox))
Bks = Button(root, text='BS', padx=20, pady=4, bg="#ff6242", fg="#ffffff", command=lambda: utilBtn('BS', inputBox))
Clr = Button(root, text='Clr', padx=20, pady=113, bg="#a9a9a9", fg="#ffffff", command=lambda: utilBtn('Clr', inputBox))

decpt.grid(row=5, column=2)
Bks.grid(row=0, column=5)
Clr.grid(row=2, column=5, rowspan=4)

buttons.extend([Add, Sub, Mul, Div, paro, parc, Eq, Bks, Clr])

# Keep the window running
root.mainloop()

#####################################################################################################i#####################################

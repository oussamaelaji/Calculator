#-----------------------------------------------#
#   ___                                         #
#  / _ \ _   _ ___ ___  __ _ _ __ ___   __ _    #
# | | | | | | / __/ __|/ _` | '_ ` _ \ / _` |   #
# | |_| | |_| \__ \__ \ (_| | | | | | | (_| |   #
#  \___/ \__,_|___/___/\__,_|_| |_| |_|\__,_|   #
#                                               #
#-----------------------------------------------#

import tkinter as tk
from tkinter import ttk, E, Frame, LEFT, StringVar


def labelmessage(num):
    global value, num1, num2, op, calc, tempnum
    Operator = ["+", "-", "*", "/"]
    if num == ".":  # num = "."
        value = value + num
        data.set(value)
    elif num == "CE":
        value = '0'
        data.set(value)
    elif num == "C":
        value = '0'
        data.set(value)
        dataTot.set('')
    elif num == "DEL":
        value = value[:len(value)-1]
        data.set(value)
    elif num in Operator:
        op = num
        num1 = value
        value = value + num
        dataTot.set(value)
        value = '0'
    elif not(num in Operator) and not(num == "="):  # num = number
        if value == '0':  # if number starts with 0 exemple 03 => 3
            value = num
        else:
            value += num
        num2 = value
        data.set(value)
    else:  # num = "="
        if num2 == "0" and op == "/":  # if num1/0 => Cannot divided by 0
            dataTot.set('')
            data.set('Cannot divided by 0')
        else:
            value = '0'
            tempnum = str(eval(num1+op+num2))
            if float(tempnum) == int(float(tempnum)):  # for exemple if 8/2 result is 4 not 4.0
                data.set(int(float(tempnum)))
                tempnum = str(int(float(tempnum)))
            else:  # for exemple if 1/3 result is 0.33333333
                data.set(f"{tempnum:.10}")  # print 10 caractere included .
            dataTot.set(num1+op+num2+num)
    if not(tempnum == '') and (num in Operator):  # Num = +-*/
        value = tempnum
        num2 = value
        dataTot.set(value)
        tempnum = ''
        labelmessage(op)
    elif not(tempnum == '') and not(num in Operator) and not(num == "="):  # num = number
        tempnum = ''
        dataTot.set('')


def button0(event):
    btn0['bg'] = "#d8dee6"


def button1(event):
    btn1['bg'] = "#d8dee6"


def button2(event):
    btn2['bg'] = "#d8dee6"


def button3(event):
    btn3['bg'] = "#d8dee6"


def button4(event):
    btn4['bg'] = "#d8dee6"


def button5(event):
    btn5['bg'] = "#d8dee6"


def button6(event):
    btn6['bg'] = "#d8dee6"


def button7(event):
    btn7['bg'] = "#d8dee6"


def button8(event):
    btn8['bg'] = "#d8dee6"


def button9(event):
    btn9['bg'] = "#d8dee6"


def button10(event):
    btn10['bg'] = "#d8dee6"


def button11(event):
    btn11['bg'] = "#d8dee6"


def button12(event):
    btn12['bg'] = "#d8dee6"


def button13(event):
    btn13['bg'] = "#d8dee6"


def button14(event):
    btn14['bg'] = "#d8dee6"


def button15(event):
    btn15['bg'] = "#d8dee6"


def button16(event):
    btn16['bg'] = "#d8dee6"


def button17(event):
    btn17['bg'] = "#d8dee6"


def button18(event):
    btn18['bg'] = "#3582e8"


def Leavebutton0(event):
    btn0['bg'] = "SystemButtonFace"  # return to default value


def Leavebutton1(event):
    btn1['bg'] = "SystemButtonFace"


def Leavebutton2(event):
    btn2['bg'] = "SystemButtonFace"


def Leavebutton3(event):
    btn3['bg'] = "SystemButtonFace"


def Leavebutton4(event):
    btn4['bg'] = "SystemButtonFace"


def Leavebutton5(event):
    btn5['bg'] = "SystemButtonFace"


def Leavebutton6(event):
    btn6['bg'] = "SystemButtonFace"


def Leavebutton7(event):
    btn7['bg'] = "SystemButtonFace"


def Leavebutton8(event):
    btn8['bg'] = "SystemButtonFace"


def Leavebutton9(event):
    btn9['bg'] = "SystemButtonFace"


def Leavebutton10(event):
    btn10['bg'] = "SystemButtonFace"


def Leavebutton11(event):
    btn11['bg'] = "SystemButtonFace"


def Leavebutton12(event):
    btn12['bg'] = "SystemButtonFace"


def Leavebutton13(event):
    btn13['bg'] = "SystemButtonFace"


def Leavebutton14(event):
    btn14['bg'] = "SystemButtonFace"


def Leavebutton15(event):
    btn15['bg'] = "SystemButtonFace"


def Leavebutton16(event):
    btn16['bg'] = "SystemButtonFace"


def Leavebutton17(event):
    btn17['bg'] = "SystemButtonFace"


def Leavebutton18(event):
    btn18['bg'] = "#5ea0f7"


root = tk.Tk()
root.geometry('300x400')
root.resizable(0, 0)
root.title('Calculator')
data = StringVar()
dataTot = StringVar()
value = '0'
num1, num2, tempnum = '0', '', ''
op = ''
calc = False
data.set(value)
Label1 = tk.Label(root, text="Label", textvariable=dataTot, anchor=E, font=("Arial", 12),
                  background="#d8dee6", foreground="black")
Label1.pack(expand=False, fill="both")
Label = tk.Label(root, text="Label", textvariable=data, anchor=E, font=("Arial", 20, "bold"),
                 background="#d8dee6", foreground="black")
Label.pack(expand=False, fill="both")
Frame1 = Frame(root)
Frame1.pack(expand=True, fill="both")
Frame2 = Frame(root)
Frame2.pack(expand=True, fill="both")
Frame3 = Frame(root)
Frame3.pack(expand=True, fill="both")
Frame4 = Frame(root)
Frame4.pack(expand=True, fill="both")
Frame5 = Frame(root)
Frame5.pack(expand=True, fill="both")
btn0 = tk.Button(Frame1, text="CE", font=("Verdana", 22), border=0, width=2,
                 command=lambda: labelmessage("CE"))
btn0.pack(side=LEFT, expand=True, fill="both")
btn1 = tk.Button(Frame1, text="C", font=("Verdana", 22), border=0, width=2,
                 command=lambda: labelmessage("C"))
btn1.pack(side=LEFT, expand=True, fill="both")
btn2 = tk.Button(Frame1, text="DEL", font=("Verdana", 22), border=0, width=2,
                 command=lambda: labelmessage("DEL"))
btn2.pack(side=LEFT, expand=True, fill="both")
btn3 = tk.Button(Frame1, text="/", font=("Verdana", 22), border=0, width=2,
                 command=lambda: labelmessage("/"))
btn3.pack(side=LEFT, expand=True, fill="both")
btn4 = tk.Button(Frame2, text="7", font=("Verdana", 22), border=0,
                 command=lambda: labelmessage("7"))
btn4.pack(side=LEFT, expand=True, fill="both")
btn5 = tk.Button(Frame2, text="8", font=("Verdana", 22), border=0,
                 command=lambda: labelmessage("8"))
btn5.pack(side=LEFT, expand=True, fill="both")
btn6 = tk.Button(Frame2, text="9", font=("Verdana", 22), border=0,
                 command=lambda: labelmessage("9"))
btn6.pack(side=LEFT, expand=True, fill="both")
btn7 = tk.Button(Frame2, text="*", font=("Verdana", 22), border=0, width=2,
                 command=lambda: labelmessage("*"))
btn7.pack(side=LEFT, expand=True, fill="both")
btn8 = tk.Button(Frame3, text="4", font=("Verdana", 22), border=0,
                 command=lambda: labelmessage("4"))
btn8.pack(side=LEFT, expand=True, fill="both")
btn9 = tk.Button(Frame3, text="5", font=("Verdana", 22), border=0,
                 command=lambda: labelmessage("5"))
btn9.pack(side=LEFT, expand=True, fill="both")
btn10 = tk.Button(Frame3, text="6", font=("Verdana", 22), border=0,
                  command=lambda: labelmessage("6"))
btn10.pack(side=LEFT, expand=True, fill="both")
btn11 = tk.Button(Frame3, text="-", font=("Verdana", 22), border=0, width=2,
                  command=lambda: labelmessage("-"))
btn11.pack(side=LEFT, expand=True, fill="both")
btn12 = tk.Button(Frame4, text="1", font=("Verdana", 22), border=0,
                  command=lambda: labelmessage("1"))
btn12.pack(side=LEFT, expand=True, fill="both")
btn13 = tk.Button(Frame4, text="2", font=("Verdana", 22), border=0,
                  command=lambda: labelmessage("2"))
btn13.pack(side=LEFT, expand=True, fill="both")
btn14 = tk.Button(Frame4, text="3", font=("Verdana", 22), border=0,
                  command=lambda: labelmessage("3"))
btn14.pack(side=LEFT, expand=True, fill="both")
btn15 = tk.Button(Frame4, text="+", font=("Verdana", 22), border=0, width=2,
                  command=lambda: labelmessage("+"))
btn15.pack(side=LEFT, expand=True, fill="both")
btn16 = tk.Button(Frame5, text="0", font=("Verdana", 22), border=0,
                  command=lambda: labelmessage("0"))
btn16.pack(side=LEFT, expand=True, fill="both")
btn17 = tk.Button(Frame5, text=".", font=("Verdana", 22), border=0,
                  command=lambda: labelmessage('.'))
btn17.pack(side=LEFT, expand=True, fill="both")
btn18 = tk.Button(Frame5, text="=", font=("Verdana", 22), border=0, bg="#5ea0f7",
                  command=lambda: labelmessage('='))
btn18.pack(side=LEFT, expand=True, fill="both")
btn0.bind("<Enter>", button0)
btn1.bind("<Enter>", button1)
btn2.bind("<Enter>", button2)
btn3.bind("<Enter>", button3)
btn4.bind("<Enter>", button4)
btn5.bind("<Enter>", button5)
btn6.bind("<Enter>", button6)
btn7.bind("<Enter>", button7)
btn8.bind("<Enter>", button8)
btn9.bind("<Enter>", button9)
btn10.bind("<Enter>", button10)
btn11.bind("<Enter>", button11)
btn12.bind("<Enter>", button12)
btn13.bind("<Enter>", button13)
btn14.bind("<Enter>", button14)
btn15.bind("<Enter>", button15)
btn16.bind("<Enter>", button16)
btn17.bind("<Enter>", button17)
btn18.bind("<Enter>", button18)
btn0.bind("<Leave>", Leavebutton0)
btn1.bind("<Leave>", Leavebutton1)
btn2.bind("<Leave>", Leavebutton2)
btn3.bind("<Leave>", Leavebutton3)
btn4.bind("<Leave>", Leavebutton4)
btn5.bind("<Leave>", Leavebutton5)
btn6.bind("<Leave>", Leavebutton6)
btn7.bind("<Leave>", Leavebutton7)
btn8.bind("<Leave>", Leavebutton8)
btn9.bind("<Leave>", Leavebutton9)
btn10.bind("<Leave>", Leavebutton10)
btn11.bind("<Leave>", Leavebutton11)
btn12.bind("<Leave>", Leavebutton12)
btn13.bind("<Leave>", Leavebutton13)
btn14.bind("<Leave>", Leavebutton14)
btn15.bind("<Leave>", Leavebutton15)
btn16.bind("<Leave>", Leavebutton16)
btn17.bind("<Leave>", Leavebutton17)
btn18.bind("<Leave>", Leavebutton18)
tk.mainloop()

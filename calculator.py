from tkinter import *
def button_click(xyz):
    abc = a.get()
    a.delete(0, END)
    a.insert(0, str(abc) + str(xyz))
def clear():
    a.delete(0, END)
def add():
    num_1 = a.get()
    global num
    global work
    num = int(num_1)
    work = "add"
    a.delete(0,END)
def multi():
    num_1 = a.get()
    global num
    global work
    num = int(num_1)
    work = "multi"
    a.delete(0,END)
def divi():
    num_1 = a.get()
    global num
    global work
    num = int(num_1)
    work = "divi"
    a.delete(0, END)
def sub():
    num_1 = a.get()
    global num
    global work
    num = int(num_1)
    work = "sub"
    a.delete(0, END)
def equal():
    num_2 = a.get()
    a.delete(0,END)
    if work == "add":
        a.insert(0, num + int(num_2))
    if work == "multi":
        a.insert(0, num * int(num_2))
    if work == "sub":
        a.insert(0, num - int(num_2))
    if work == "divi":
        a.insert(0, num / int(num_2))
root = Tk()
root.title(" Calculator")
root.resizable(False, False)
root.configure(bg="#00ffd0")
a = Entry(root, font=('', '30', 'bold'), bg="#8800ff", fg="red", justify="left", bd=40)
a.grid(columnspan=4)
buttton__1 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="1", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(1))
buttton__1.grid(row=1, column=0)
buttton__2 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="2", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(2))
buttton__2.grid(row=1, column=1)
buttton__3 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="3", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(3))
buttton__3.grid(row=1, column=2)
buttton__4 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="4", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(4))
buttton__4.grid(row=2, column=0)
buttton__5 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="5", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(5))
buttton__5.grid(row=2, column=1)
buttton__6 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="6", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(6))
buttton__6.grid(row=2, column=2)
buttton__7 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="7", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(7))
buttton__7.grid(row=3, column=0)
buttton__8 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="8", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(8))
buttton__8.grid(row=3, column=1)
buttton__9 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="9", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(9))
buttton__9.grid(row=3, column=2)
buttton__0 = Button(root, font=('', '30', 'bold'), bg="#ff0062", fg="black", text="0", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
button_click(0))
buttton__0.grid(row=4, column=1)
buttton__add = Button(root, font=('', '30', 'bold'), bg="#0800ff", fg="black", text="+", bd=14,
pady=10, padx=20,
activebackground="black",
activeforeground="#ff0062",command=lambda:add())
buttton__add.grid(row=1, column=3)
buttton__equal = Button(root, font=('', '30', 'bold'), bg="#0800ff", fg="black", text="=", bd=14,
pady=10, padx=20,
activebackground="black",
activeforeground="#ff0062",command=lambda:equal())
buttton__equal.grid(row=4, column=2)
buttton__clear = Button(root, font=('', '30', 'bold'), bg="#0800ff", fg="black", text="c", bd=14,
pady=10, padx=20,
activebackground="black", activeforeground="#ff0062", command=lambda:
clear())
buttton__clear.grid(row=4, column=0)
buttton__multi = Button(root, font=('', '30', 'bold'), bg="#0800ff", fg="black", text="*", bd=14,
pady=10, padx=20,
activebackground="black",
activeforeground="#ff0062",command=lambda:multi())
buttton__multi.grid(row=3, column=3)
buttton__sub = Button(root, font=('', '30', 'bold'), bg="#0800ff", fg="black", text="-", bd=14,
pady=10, padx=20,
activebackground="black",
activeforeground="#ff0062",command=lambda:sub())
buttton__sub.grid(row=2, column=3)
buttton__divi = Button(root, font=('', '30', 'bold'), bg="#0800ff", fg="black", text="/", bd=14,
pady=10, padx=20,
activebackground="black",
activeforeground="#ff0062",command=lambda:divi())
buttton__divi.grid(row=4, column=3)
root.mainloop()
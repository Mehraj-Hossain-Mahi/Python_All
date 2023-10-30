from tkinter import *

root = Tk()
root.title("Registration")
root.geometry("600x470")
root.resizable(False,False)


def register():
    print("Registered")

Label(root,text="Python Registration Form", front='airal 25').pack(pady=50)
Label(text="Name",font=23).place(x=100,y=150)

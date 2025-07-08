from tkinter import *
from datetime import date

root = Tk()
root.title('gettting started with widgets')
root.geometry('400x300')

lbl = Label(Text="hey there!", fg="white",bg="#072F5F", height=1,width=300)
name_lbl = Label(text="full name",bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message 
    message = "welcome to the application! \nToday's date is:"
    greet = "hello"+name+"\n"

    text_box.insert(END,greet)
    text.box.insert

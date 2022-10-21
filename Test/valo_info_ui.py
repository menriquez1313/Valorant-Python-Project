from logging import root
from random import choices
from sqlite3 import Row
from tkinter import *
from tkinter.ttk import *

from numpy import column_stack


window = Tk()
window.title("Valorant Information Project")
window.config(padx=20, pady=20)
window.minsize(width=300, height=600)


# #User Entry
# choice = Entry(width=10)
# choice.grid(column=1, row=1)
# choice.place(relx=0.5, rely=0.5, anchor=S)


# list_choice = ("1: User and locale", "2: Update/Status on Valorant","3: Current Act Info", "4: Current Agents", "5: Current Maps", "5: Current Maps" )
# list = StringVar(list_choice)

#User Options
option = Label(text="What would you like to view?")
option.grid(column=1, row=0)

"""  print("/////////Welcome to VALORANT info///////")
    print("1: User and locale")
    print("2: Update/Status on Valorant")
    print("3: Current Act Info")
    print("4: Current Agents")
    print("5: Current Maps")
    print("0: Exit")
"""

choices = Listbox(height=6)
choices.grid(column=1,row=1)
choices.insert(END, "1: User and locale")
choices.insert(END, "2: Update/Status on Valorant")
choices.insert(END, "3: Current Act Info")
choices.insert(END, "4: Current Agents")
choices.insert(END, "5: Current Maps")
choices.insert(END, "0: Exit")

select = Button(text="Select")
select.grid(column=1,row=2)







window.mainloop()
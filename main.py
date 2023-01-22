import tkinter as tk
import csv

amount = 0

def update_max(event):
    print("you pressed the update button")
    print(field_max.get())
    field_max.delete(0, tk.END)

def update_total(event):
    print("you pressed the add button")
    field_curr_spent.insert(0, field_add.get())
    field_add.delete(0, tk.END)
    #amount += button_add.get()

window = tk.Tk()  # creates a window

# set window information
window.title("Saving Assistant 4000")  # window title
window.geometry("300x200")  # window width x height

spendingMax = tk.Label(text="Max Monthly Spending")
spendingMax.grid(column=0, row=0)

field_max = tk.Entry(window)
field_max.grid(column=1, row=0)

updateMax = tk.Button(window, text="Update")
updateMax.grid(column=2, row=0)
updateMax.bind("<Button-1>", update_max)

label_spent = tk.Label(text="Amount Spent So Far")
label_spent.grid(column=0, row=1)

field_curr_spent = tk.Entry(window)
field_curr_spent.grid(column=1, row=1)

label_add = tk.Label(text="Add New Expense")
label_add.grid(column=0, row=2)

field_add = tk.Entry(window)
field_add.grid(column=1, row=2)

button_add = tk.Button(window, text="Add")
button_add.grid(column=2, row=2)
button_add.bind("<Button-1>", update_total)

window.mainloop()  # need to call this just before running any tkinter app

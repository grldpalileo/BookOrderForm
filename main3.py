from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


def update_level1_state():
    if checkbox1_var.get() == 1:
        Level1.config(state="readonly")
        Quantity1_entry.config(state="normal")

    else:
        Level1.set("")
        Level1.config(state="disabled")
        Quantity1.set("")
        Quantity1_entry.config(state="disabled")
        UnitPrice1.set("")


def update_level2_state():
    if checkbox2_var.get() == 1:
        Level2.config(state="readonly")
        Quantity2_entry.config(state="normal")

    else:
        Level2.set("")
        Level2.config(state="disabled")
        Quantity2.set("")
        Quantity2_entry.config(state="disabled")
        UnitPrice2.set("")


def update_level3_state():
    if checkbox3_var.get() == 1:
        Level3.config(state="readonly")
        Quantity3_entry.config(state="normal")
    else:
        Level3.set("")
        Level3.config(state="disabled")
        Quantity3.set("")
        Quantity3_entry.config(state="disabled")
        UnitPrice3.set("")


def compute():
    subtotals = []

    if checkbox1_var.get() == 1:
        quantity = Quantity1.get()
        unit_price = UnitPrice1.get()
        if quantity.isdigit():
            subtotal = float(unit_price) * int(quantity)
            SubTotal1.set(int(subtotal))
            subtotals.append(subtotal)
        else:
            messagebox.showerror("Error", "Please enter a valid quantity for Book 1.")

    if checkbox2_var.get() == 1:
        quantity = Quantity2.get()
        unit_price = UnitPrice2.get()
        if quantity.isdigit():
            subtotal = float(unit_price) * int(quantity)
            SubTotal2.set(int(subtotal))
            subtotals.append(subtotal)
        else:
            messagebox.showerror("Error", "Please enter a valid quantity for Book 2.")

    if checkbox3_var.get() == 1:
        quantity = Quantity3.get()
        unit_price = UnitPrice3.get()
        if quantity.isdigit():
            subtotal = float(unit_price) * int(quantity)
            SubTotal3.set(int(subtotal))
            subtotals.append(subtotal)
        else:
            messagebox.showerror("Error", "Please enter a valid quantity for Book 3.")

    TotalAmount.set(sum(subtotals))


def clear():
    checkbox1_var.set(0)
    checkbox2_var.set(0)
    checkbox3_var.set(0)
    Level1.set("")
    Level2.set("")
    Level3.set("")
    UnitPrice1.set("")
    UnitPrice2.set("")
    UnitPrice3.set("")
    Quantity1.set("")
    Quantity2.set("")
    Quantity3.set("")
    SubTotal1.set(0)
    SubTotal2.set(0)
    SubTotal3.set(0)
    TotalAmount.set(0)

    Level1.config(state="disabled")
    Quantity1_entry.config(state="disabled")
    Level1.set("")
    Quantity1.set("")

    Level2.config(state="disabled")
    Quantity2_entry.config(state="disabled")
    Level2.set("")
    Quantity2.set("")

    Level3.config(state="disabled")
    Quantity3_entry.config(state="disabled")
    Level3.set("")
    Quantity3.set("")


def get_unit_price(level):
    if level == "NURSERY":
        return "150.00"
    elif level == "KINDER":
        return "200.00"
    elif level == "PREP":
        return "250.00"
    else:
        return ""


def update_unit_price1(event):
    level = Level1.get()
    unit_price = get_unit_price(level)
    UnitPrice1.set(unit_price)


def update_unit_price2(event):
    level = Level2.get()
    unit_price = get_unit_price(level)
    UnitPrice2.set(unit_price)


def update_unit_price3(event):
    level = Level3.get()
    unit_price = get_unit_price(level)
    UnitPrice3.set(unit_price)


root = Tk()
root.geometry("700x215")
root.title("Book Order Form")

Label(root, text="MJN Book Store", font="tahoma 10 bold").place(x=280, y=5)
Label(root, text="Book Title", font="tahoma 10 bold").place(x=35, y=35)
Label(root, text="Level", font="tahoma 10 bold").place(x=210, y=35)
Label(root, text="Unit Price", font="tahoma 10 bold").place(x=330, y=35)
Label(root, text="Quantity", font="tahoma 10 bold").place(x=470, y=35)
Label(root, text="Sub-Total", font="tahoma 10 bold").place(x=595, y=35)
Label(root, text="Total Amount:", font="tahoma 10").place(x=490, y=170)

checkbox1_var = IntVar()
checkbox2_var = IntVar()
checkbox3_var = IntVar()

checkbox1 = Checkbutton(root, text="Everyday English", font="tahoma 10", variable=checkbox1_var, state="normal", command=update_level1_state)
checkbox1.place(x=15, y=55)
checkbox2 = Checkbutton(root, text="Integrated Mathematics", font="tahoma 10", variable=checkbox2_var, state="normal", command=update_level2_state)
checkbox2.place(x=15, y=85)
checkbox3 = Checkbutton(root, text="Wonders of Science", font="tahoma 10", variable=checkbox3_var, state="normal", command=update_level3_state)
checkbox3.place(x=15, y=115)

Level1 = Combobox(root, values=['', 'NURSERY', 'KINDER', 'PREP'], font="tahoma 10", width=12, state="disabled")
Level1.place(x=180, y=55)
Level1.bind("<<ComboboxSelected>>", update_unit_price1)

Level2 = Combobox(root, values=['', 'NURSERY', 'KINDER', 'PREP'], font="tahoma 10", width=12, state="disabled")
Level2.place(x=180, y=85)
Level2.bind("<<ComboboxSelected>>", update_unit_price2)

Level3 = Combobox(root, values=['', 'NURSERY', 'KINDER', 'PREP'], font="tahoma 10", width=12, state="disabled")
Level3.place(x=180, y=115)
Level3.bind("<<ComboboxSelected>>", update_unit_price3)

UnitPrice1 = StringVar()
UnitPrice1_entry = Entry(root, textvariable=UnitPrice1, width=14, font="tahoma 10", state="readonly")
UnitPrice1_entry.place(x=315, y=55)

UnitPrice2 = StringVar()
UnitPrice2_entry = Entry(root, textvariable=UnitPrice2, width=14, font="tahoma 10", state="readonly")
UnitPrice2_entry.place(x=315, y=85)

UnitPrice3 = StringVar()
UnitPrice3_entry = Entry(root, textvariable=UnitPrice3, width=14, font="tahoma 10", state="readonly")
UnitPrice3_entry.place(x=315, y=115)

Quantity1 = StringVar()
Quantity1_entry = Entry(root, textvariable=Quantity1, width=14, font="tahoma 10", state="disabled")
Quantity1_entry.place(x=450, y=55)

Quantity2 = StringVar()
Quantity2_entry = Entry(root, textvariable=Quantity2, width=14, font="tahoma 10", state="disabled")
Quantity2_entry.place(x=450, y=85)

Quantity3 = StringVar()
Quantity3_entry = Entry(root, textvariable=Quantity3, width=14, font="tahoma 10", state="disabled")
Quantity3_entry.place(x=450, y=115)

SubTotal1 = IntVar()
SubTotal1_entry = Entry(root, textvariable=SubTotal1, width=14, font="tahoma 10", state="readonly")
SubTotal1_entry.place(x=580, y=55)

SubTotal2 = IntVar()
SubTotal2_entry = Entry(root, textvariable=SubTotal2, width=14, font="tahoma 10", state="readonly")
SubTotal2_entry.place(x=580, y=85)

SubTotal3 = IntVar()
SubTotal3_entry = Entry(root, textvariable=SubTotal3, width=14, font="tahoma 10", state="readonly")
SubTotal3_entry.place(x=580, y=115)

TotalAmount = DoubleVar()
TotalAmount_entry = Entry(root, textvariable=TotalAmount, width=14, font="tahoma 10", state="readonly")
TotalAmount_entry.place(x=580, y=170)

compute_button = Button(root, text="COMPUTE", width=15, font="tahoma 12", state="normal", command=compute)
compute_button.place(x=55, y=160)

clear_button = Button(root, text="CLEAR", width=15, font="tahoma 12", state="normal", command=clear)
clear_button.place(x=210, y=160)

checkbox1.deselect()
checkbox2.deselect()
checkbox3.deselect()

root.mainloop()

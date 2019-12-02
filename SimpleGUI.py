# This program will keep track of every medical device in the inventory
# Basic functions:  add items, remove items, and view the current inventory
# Simple GUI
# The code will open a GUI from where you can enter the serial_number, type and name of the item you want to manipulate

import tkinter


class Inventory:
    # Constructor
    def __init__(self):
        self.inventory_dict = {}
        self.show_text = tkinter.StringVar()

    # AddItem adds a new item if it does-not already exists and also if the new item is not blank
    def addItem(self, type, name, serial_number):
        if serial_number not in self.inventory_dict and (serial_number != "" or name != "" or type != ""):
            self.inventory_dict[serial_number] = [type, name]
            # return self.inventory_dict
            self.show_text.set(self.inventory_dict)
        else:
            error_msg = "Either Item already exist Or you have tried to add null item"
            # return error_msg
            self.show_text.set(error_msg)

    # Remove the item specified by the serial number if the serial number specified is not blank
    def removeItem(self, serial_number):
        if serial_number in self.inventory_dict and serial_number != "":
            self.inventory_dict.pop(serial_number)
            # return self.inventory_dict
            self.show_text.set(self.inventory_dict)
        else:
            error_msg = "Item does-not exist Or you have tried to remove null item"
            # return error_msg
            self.show_text.set(error_msg)

    # View the inventory
    def viewInventory(self):
        self.show_text.set(self.inventory_dict)

    # Create the window with elements
    def drawWindow(self, master):
        master.title("Inventory Management System")
        inv = Inventory()
        tkinter.Label(master, text="Serial number").grid(row=5)
        self.sr_no = tkinter.Entry(master)
        self.sr_no.grid(row=5, column=1)
        tkinter.Label(master, text="Type").grid(row=7)
        self.type = tkinter.Entry(master)
        self.type.grid(row=7, column=1)
        tkinter.Label(master, text="Name").grid(row=9)
        self.name = tkinter.Entry(master)
        self.name.grid(row=9, column=1)

        tkinter.Button(master, text="Add item", fg="red",
                       command=lambda: self.addItem(self.type.get(), self.name.get(), self.sr_no.get())).grid(row=10,
                                                                                                              column=1)
        tkinter.Button(master, text="Remove item", fg="red", command=lambda: self.removeItem(self.sr_no.get())).grid(
            row=10, column=2)
        tkinter.Button(master, text="View item", fg="red", command=lambda: self.viewInventory()).grid(row=10, column=3)
        tkinter.Label(master, text="Inventory items displayed").grid()
        tkinter.Label(master, textvariable=self.show_text).grid()


if __name__ == '__main__':
    root = tkinter.Tk()
    window = Inventory()
    window.drawWindow(root)
    root.mainloop()

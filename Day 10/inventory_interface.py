import tkinter as tk
from tkinter import messagebox
from inventory import Inventory

class InventoryInterface:

    def __init__(self, root):
        self.root = root
        self.root.title("RPG Inventory")
        self.inventory = Inventory()

        self.entry_item = tk.Entry(root)
        self.entry_item.pack(pady=5)

        # Buttons
        self.btn_add = tk.Button(root, text="Add Item", command=self.add_item)
        self.btn_add.pack(pady=5)

        self.btn_remove = tk.Button(root, text="Remove Item", command=self.remove_item)
        self.btn_remove.pack(pady=5)

        self.frame_items = tk.Frame(root)
        self.frame_items.pack(pady=10)

        self.update_interface()

    def add_item(self):
        name = self.entry_item.get()
        if name:
            if self.inventory.add_item(name):
                self.update_interface()
            else:
                messagebox.showwarning("Inventory is full", "There's no more space in your inventory!")

    def remove_item(self):
        name = self.entry_item.get()
        if name:
            if self.inventory.remove_item(name):
                self.update_interface()
            else:
                messagebox.showwarning("Item not found", "This item is not in the inventory!")

    def update_interface(self):
        for widget in self.frame_items.winfo_children():
            widget.destroy()

        for item in self.inventory.slots:
            lbl = tk.Label(self.frame_items, text=f"{item.name} x{item.quantity}")
            lbl.pack()
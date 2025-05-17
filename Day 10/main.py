import tkinter as tk
from inventory_interface import InventoryInterface

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryInterface(root)
    root.mainloop()

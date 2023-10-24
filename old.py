from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from interface import*
from modiflyPlugin import*
from export import*
class myGui:
    selectedItem = "None"
def refresh(root):
    # Tk.update(root)
    root.destroy()
    main() 
def checkAndRefresh(root):
    checkAll()
    refresh(root)
def updateAndRefresh(root):
    updateAll()
    refresh(root)


def main():
    DATA = getData()
    root = tk.Tk()
    root.title('Honzer\'s Plugin Manager')
    # root.geometry("1x400")
    treeview = ttk.Treeview(root, show="headings", columns=("Name", "Rollno", "Marks","Date"),selectmode ='browse')
    treeview.heading("#1", text="Name")
    treeview.heading("#2", text="Version")
    treeview.heading("#3", text="Status")
    treeview.heading("#4", text="Date")
    treeview.grid()
    treeview.pack(side ='right')
    verscrlbar = ttk.Scrollbar(root, orient ="vertical", command = treeview.yview)
    verscrlbar.pack(side ='right', fill ='x')
    treeview.configure(xscrollcommand = verscrlbar.set)

    for row in DATA:
        treeview.insert("", "end", values=(row["Name"], row["AssemblyVersion"], row["Status"], row["Date"]))
        # treeview.insert("", "end", values=(row["Name"], row["Rollno"], row["Marks"]))
    def selectItem(a):#  Select item by clicking treeview
        curItem = treeview.focus()
        print(treeview.item(curItem))
        itemNameTemp = treeview.item(curItem)       
        myGui.selectedItem = itemNameTemp['values'][0]
    treeview.bind('<ButtonRelease-1>', selectItem)

    b1 = Button(root, text="Refresh", bg="lightblue", width=10,command=lambda : refresh(root))
    b2 = Button(root, text="Check", bg="lightblue", width=10,command=lambda : checkAndRefresh(root))
    b3 = Button(root, text="UpdateAll", bg="lightblue", width=10,command=lambda : updateAndRefresh(root))
    b1.pack()
    b2.pack()
    b3.pack()
    textBox = tk.Entry(root,width=13) 
    textBox.pack()

    def addPluginFromInput():
        text = textBox.get()
        addPlugin(text)
        refresh(root)
    def removePlugin():
        popPlugin(myGui.selectedItem)
        refresh(root)

    b4 = Button(root, text="Add", bg="lightblue", width=10,command=lambda : addPluginFromInput())
    b5 = Button(root, text="Remove", bg="lightblue", width=10,command=lambda : removePlugin())
    b4.pack()
    b5.pack()
    textBox2 = tk.Entry(root,width=13) 
    textBox2.pack()
    def addJsonFromInput():
        text = textBox2.get()
        addJson(text)
        refresh(root)
    b6 = Button(root, text="AddLink", bg="lightblue", width=10,command=lambda : addJsonFromInput())
    b6.pack()
    b7 = Button(root, text="Export", bg="lightgreen", width=10,command=lambda : export())
    b7.pack()

    root.mainloop()


main()
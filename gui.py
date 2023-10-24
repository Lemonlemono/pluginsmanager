from tkinter import Tk, Button
import tkinter as tk
import tkinter.ttk as ttk
from interface import*
from modiflyPlugin import*
from export import*
import sys
from tkinter.scrolledtext import ScrolledText

class MyButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#0052cc'
        self['fg'] = '#ffffff'
        self['bd'] = 0
        self['activebackground']='#003380'
        self['activeforeground']='#aaffaa'
        self['width'] = 10
class PrintLogger(object):  # create file like object

    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.configure(state="normal")  # make field editable
        self.textbox.insert("end", text)  # write text to textbox
        self.textbox.see("end")  # scroll to end
        self.textbox.configure(state="disabled")  # make field readonly

    def flush(self):  # needed for file like object
        pass
class myGui(Tk):

    def __init__(self):
        self.switchTrigger = False
        super().__init__()
        self.selectedItem = "None"
        DATA = getData()
        # self = Tk()
        self.title('Honzer\'s Plugin Manager')
        # root.geometry("1x400")
        self.treeview = ttk.Treeview(self, show="headings", columns=("Name", "Rollno", "Marks","Date"),selectmode ='browse')
        self.treeview.heading("#1", text="Name")
        self.treeview.heading("#2", text="Version")
        self.treeview.heading("#3", text="Status")
        self.treeview.heading("#4", text="Date")
        self.treeview.grid(row=0, column=1, columnspan = 1, rowspan = 7, padx = 2, pady = 5)
        self.verscrlbar = ttk.Scrollbar(self, orient ="vertical", command = self.treeview.yview)
        self.verscrlbar.grid(row = 0,column=2,rowspan = 9)
        self.treeview.configure(xscrollcommand = self.verscrlbar.set)

        for row in DATA:
            self.treeview.insert("", "end", values=(row["Name"], row["AssemblyVersion"], row["Status"], row["Date"]))

        def selectItem(a):#  Select item by clicking treeview
            curItem = self.treeview.focus()
            # print(self.treeview.item(curItem))
            itemNameTemp = self.treeview.item(curItem)
            if itemNameTemp['values'] != "":
                self.selectedItem = str(itemNameTemp['values'][0])
        
        self.treeview.bind('<ButtonRelease-1>', selectItem)
        self.textBox = tk.Entry(self,width=12,bg="#bfbfbf") 
        self.textBox2 = tk.Entry(self,width=12,bg="#bfbfbf") 
        b1 = MyButton(self, text="Refresh",command=lambda : self.refreshTree())
        b1.config(activebackground="#cc8800",bg = "#ff9933")
        b2 = MyButton(self, text="Check",command=lambda : self.checkAndRefresh())
        b3 = MyButton(self, text="UpdateAll",command=lambda : self.updateAndRefresh())
        b4 = MyButton(self, text="Add", command=lambda : self.addPluginFromInput())
        b5 = MyButton(self, text="Remove",command=lambda : self.removePlugin())
        b6 = MyButton(self, text="Manager",command=lambda : self.switchWindow2())
        b7 = MyButton(self, text="Export",command=lambda : export(str(self.textBox2.get())))
        b7.config(bg="#33cc33",activebackground="#248f24")

        b1.grid(row=0, column=0, pady=3)
        b2.grid(row=1, column=0, pady=3)
        b3.grid(row=2, column=0, pady=3)
        b4.grid(row=4, column=0, pady=3)
        b5.grid(row=5, column=0, pady=3)
        b6.grid(row=6, column=0, pady=3,padx=2)
        b7.grid(row=8, column=0, pady=3,padx=2)
        self.textBox.grid(row=3, column=0, pady=3)
        self.textBox2.grid(row=7, column=0, pady=3)

        self.log_widget = ScrolledText(self, height=5, width=130, font=("consolas", "8", "normal"))
        self.log_widget.grid(row=7, column=1,rowspan = 3, pady=1,padx=2)
        self.redirect_logging()
        
    def switchWindow2(self):
         self.switchTrigger = True
         self.reset_logging()
         self.destroy()
    def addJsonFromInput(self):
            text = self.textBox2.get()
            addJson(text)
            self.refreshTree()

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        sys.stderr = sys.__stderr__


    def test_print(self):
        print("Am i working?")

    def redirect_logging(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger

    def addPluginFromInput(self):
            text = self.textBox.get()
            addPlugin(str(text))
            self.refreshTree()

    def removePlugin(self):
            modiflyWithName("json/avaliablePlugins.json","Name",self.selectedItem,"Status","/")
            popPlugin(str(self.selectedItem))
            self.refreshTree()

    def checkAndRefresh(self): 
            checkAll()
            self.refreshTree()

    def updateAndRefresh(self):
            updateAll()
            self.refreshTree()

    def refreshTree(self):
            DATA = getData()
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            for row in DATA:
                self.treeview.insert("", "end", values=(row["Name"], row["AssemblyVersion"], row["Status"], row["Date"]))

# if __name__ == "__main__":
#     app = myGui()
#     app.mainloop()
from tkinter import Tk, Button
import tkinter as tk
import tkinter.ttk as ttk
from interface import*
from modiflyPlugin import*
from export import*
from tkinter.scrolledtext import ScrolledText
import sys
import webbrowser as wb
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
class myGui2(Tk):

    def __init__(self):
        self.switchTrigger = False
        super().__init__()
        self.selectedItem = "None"
        DATA1 = getAvaliablePluginsData()
        # self = Tk()
        self.title('Installation Manager')
        # root.geometry("1x400")
        self.treeview = ttk.Treeview(self, show="headings", columns=("Name", "AssemblyVersion", "LastUpdate","Status","Author","No.URL"),selectmode ='browse')
        self.treeview.heading("#1", text="Name")
        self.treeview.heading("#2", text="Version")
        self.treeview.heading("#3", text="LastUpdate")
        self.treeview.heading("#4", text="Status")
        self.treeview.heading("#5", text="Author")
        self.treeview.heading("#6", text="No.URL")
        self.treeview.grid(row=0, column=1, columnspan = 4, rowspan = 1, padx = 2, pady = 5)
        self.verscrlbar = ttk.Scrollbar(self, orient ="vertical", command = self.treeview.yview)
        self.verscrlbar.grid(row = 0,column=6,rowspan = 1)
        self.treeview.configure(xscrollcommand = self.verscrlbar.set)

        for row in DATA1:
            self.treeview.insert("", "end", values=(row["Name"], row["AssemblyVersion"], row["LastUpdate"], row["Status"], row["Author"], row["No.URL"], row["DownloadLinkInstall"]))

        def selectItem(a):#  Select item by clicking treeview
            curItem = self.treeview.focus()
            # print(self.treeview.item(curItem))
            itemNameTemp = self.treeview.item(curItem)
            # if itemNameTemp['values'] != "":
            #     self.selectedItem = str(itemNameTemp['values'][0])
            self.selectedItem = {"Name": str(itemNameTemp['values'][0]),"AssemblyVersion": str(itemNameTemp['values'][1]),"DownloadLinkInstall": str(itemNameTemp['values'][6])}
        
        self.treeview.bind('<ButtonRelease-1>', selectItem)

        self.selectedItem2 = "None"
        DATA2 = getResourceListData()

        self.treeview2 = ttk.Treeview(self, show="headings", columns=("Url"),selectmode ='browse')
        self.treeview2.heading("#1", text="Url")
        self.treeview2.grid(row=0, column=6, columnspan = 3, rowspan = 1, padx = 2, pady = 5)
        self.verscrlbar2 = ttk.Scrollbar(self, orient ="vertical", command = self.treeview2.yview)
        self.verscrlbar2.grid(row = 0,column=10,rowspan = 1)
        self.treeview2.configure(xscrollcommand = self.verscrlbar.set)

        for row in DATA2:
            self.treeview2.insert("", "end", values=(row["Url"]))

        def selectItem2(a):#  Select item by clicking treeview
            curItem = self.treeview2.focus()
            # print(self.treeview2.item(curItem))
            itemNameTemp = self.treeview2.item(curItem)
            if itemNameTemp['values'] != "":
                self.selectedItem2 = str(itemNameTemp['values'][0])
        
        self.treeview2.bind('<ButtonRelease-1>', selectItem2)


        self.textBox = tk.Entry(self,width=12,bg="#bfbfbf") 
        # self.textBox2 = tk.Entry(self,width=12,bg="#bfbfbf") 
        b1 = MyButton(self, text="Refresh",command=lambda : self.refreshTree())
        b1.config(activebackground="#cc8800",bg = "#ff9933")
        b2 = MyButton(self, text="Check",command=lambda : self.checkAndRefresh())
        b3 = MyButton(self, text="Add",command=lambda : self.addPluginFromInstallation())
        b4 = MyButton(self, text="Remove", command=lambda : self.removeFromInstallation())
        b5 = MyButton(self, text="Add",command=lambda : self.addToResource())
        b6 = MyButton(self, text="Remove",command=lambda : self.removeFromResource())
        b_back = MyButton(self, text="<Back>",command=lambda : self.switchWindow1())
        b_openLink= MyButton(self, text="<Open>",command=lambda : self.openLink())
        b_openLink.config(activebackground="#33cc33",bg = "#248f24")
        
        # b7 = MyButton(self, text="Export",command=lambda : export())
        # b7.config(bg="#33cc33",activebackground="#248f24")
        b_back.grid(row=2, column=0, pady=3,padx=3)
        b1.grid(row=2, column=1, pady=3,padx=5)
        b2.grid(row=2, column=2, pady=3,padx=10)
        b3.grid(row=2, column=3, pady=3,padx=15)
        b4.grid(row=2, column=4, pady=3)
        b6.grid(row=1, column=6, pady=1,padx=3)#remove
        b_openLink.grid(row=1, column=8, pady=1,padx=3)
        self.textBox.grid(row=2, column=7, pady=1)#input
        b5.grid(row=2, column=8, pady=1,padx=3)#add
        # self.textBox2.grid(row=6, column=0, pady=3)
        self.log_widget = ScrolledText(self, height=5, width=197, font=("consolas", "8", "normal"))
        self.log_widget.grid(row=1, column=1, columnspan= 4,pady=3)
        self.redirect_logging()

    def switchWindow1(self):
        self.switchTrigger = True
        self.reset_logging()
        self.destroy()
    
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

    def test_print(self):
        print("Am i working?")

    def openLink(self):
        wb.open_new_tab(self.selectedItem2)

    def addToResource(self):
        addJson(self.textBox.get())
        self.refreshTree()
    def removeFromResource(self):
        removeObjectFromJson("json/resourceList.json","Url",self.selectedItem2)
        self.refreshTree()

    def addPluginFromInstallation(self):
        modiflyWithKey("json/avaliablePlugins.json","DownloadLinkInstall",self.selectedItem.get('DownloadLinkInstall',"NULL"),"Status","Installed")
        addPluginTest(self.selectedItem)
        self.refreshTree()

    def removeFromInstallation(self):
        modiflyWithKey("json/avaliablePlugins.json","DownloadLinkInstall",self.selectedItem.get('DownloadLinkInstall',"NULL"),"Status","/")
        popPluginTest(self.selectedItem)
        self.refreshTree()

    def checkAndRefresh(self): 
        checkAvaliablePlugins()
        self.refreshTree()

    def updateAndRefresh(self):
        updateAll()
        self.refreshTree()

    def refreshTree(self):
        DATA1 = getAvaliablePluginsData()
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        for row in DATA1:
            self.treeview.insert("", "end", values=(row["Name"], row["AssemblyVersion"], row["LastUpdate"], row["Status"], row["Author"], row["No.URL"], row["DownloadLinkInstall"]))
        DATA2 = getResourceListData()
        for item in self.treeview2.get_children():
            self.treeview2.delete(item)
        for row in DATA2:
            self.treeview2.insert("", "end", values=(row["Url"]))

# if __name__ == "__main__":
#     app = myGui2()
#     app.mainloop()
from gui import*
from managerGui import*
class main():
    shutDown=False
    while shutDown==False:
        shutDown=True
        app = myGui()
        app.mainloop()
        if app.switchTrigger ==True:
            app2 = myGui2()
            app2.mainloop()
            if app2.switchTrigger ==True:
                shutDown = False
    


if __name__ == '__main__':
    main()
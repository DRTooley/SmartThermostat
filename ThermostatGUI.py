import tkinter
import TempuratureControlLogic as TCL
import ThreadTimeValidator as TTV

class ThermostatApp(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.Initialize()
        self.threadValidator = TTV.ThreadTimeValidator()
        self.tempController = TCL.TempuratureControlLogic(self.threadValidator)

    def Initialize(self):
        self.grid()

        self.entry = tkinter.Entry(self)
        self.entry.grid(column=0, row=0, sticky='EW')

        button = tkinter.Button(self, text="Quit!", command=self.quit)
        button.grid(column=1, row=0)


    def quit(self):
        self.threadValidator.Exit()
        print("Quitting!")

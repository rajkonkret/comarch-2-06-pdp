import tkinter as tk
import tkinter.font as tkFont


# https://visualtk.com
class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_894 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_894["font"] = ft
        GLabel_894["fg"] = "#333333"
        GLabel_894["justify"] = "center"
        GLabel_894["text"] = "label"
        GLabel_894.place(x=90, y=50, width=70, height=25)

        GButton_870 = tk.Button(root)
        GButton_870["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_870["font"] = ft
        GButton_870["fg"] = "#000000"
        GButton_870["justify"] = "center"
        GButton_870["text"] = "Button"
        GButton_870.place(x=220, y=60, width=70, height=25)
        GButton_870["command"] = self.GButton_870_command

        GCheckBox_785 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_785["font"] = ft
        GCheckBox_785["fg"] = "#333333"
        GCheckBox_785["justify"] = "center"
        GCheckBox_785["text"] = "CheckBox"
        GCheckBox_785.place(x=100, y=210, width=70, height=25)
        GCheckBox_785["offvalue"] = "0"
        GCheckBox_785["onvalue"] = "1"
        GCheckBox_785["command"] = self.GCheckBox_785_command

        GRadio_334 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_334["font"] = ft
        GRadio_334["fg"] = "#333333"
        GRadio_334["justify"] = "center"
        GRadio_334["text"] = "RadioButton"
        GRadio_334.place(x=160, y=140, width=85, height=25)
        GRadio_334["command"] = self.GRadio_334_command

        GListBox_178 = tk.Listbox(root)
        GListBox_178["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_178["font"] = ft
        GListBox_178["fg"] = "#333333"
        GListBox_178["justify"] = "center"
        GListBox_178.place(x=280, y=350, width=80, height=25)

        GMessage_867 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_867["font"] = ft
        GMessage_867["fg"] = "#333333"
        GMessage_867["justify"] = "center"
        GMessage_867["text"] = "Komunikat"
        GMessage_867.place(x=300, y=240, width=80, height=25)

        GLineEdit_668 = tk.Entry(root)
        GLineEdit_668["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_668["font"] = ft
        GLineEdit_668["fg"] = "#333333"
        GLineEdit_668["justify"] = "center"
        GLineEdit_668["text"] = "Podaj wartosc"
        GLineEdit_668["relief"] = "groove"
        GLineEdit_668.place(x=420, y=120, width=70, height=25)
        GLineEdit_668["show"] = "1"

        GLabel_875 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_875["font"] = ft
        GLabel_875["fg"] = "#333333"
        GLabel_875["justify"] = "center"
        GLabel_875["text"] = "label"
        GLabel_875.place(x=90, y=410, width=70, height=25)

        GLabel_415 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_415["font"] = ft
        GLabel_415["fg"] = "#333333"
        GLabel_415["justify"] = "center"
        GLabel_415["text"] = "label"
        GLabel_415.place(x=290, y=430, width=70, height=25)

        GLabel_692 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_692["font"] = ft
        GLabel_692["fg"] = "#333333"
        GLabel_692["justify"] = "center"
        GLabel_692["text"] = "label"
        GLabel_692.place(x=450, y=390, width=70, height=25)

    def GButton_870_command(self):
        print("command")

    def GCheckBox_785_command(self):
        print("command")

    def GRadio_334_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

#!/usr/bin/python3
import tkinter as tk
import tkinter.filedialog as fd
import subprocess

class Gui:

    command = []
    window = tk.Tk()

    var_s = tk.IntVar()
    var_p = tk.IntVar()
    var_j = tk.IntVar()
    var_n = tk.IntVar()


    def button_interrupt(self):

        if self.var_s.get() == 1:
            self.command.append("-s")

        if self.var_p.get() == 1:
            self.command.append("-p")

        if self.var_j.get() == 1:
            self.command.append("-j")

        if self.var_n.get() == 1:
            self.command.append("-n")        

        print(self.command)
        subprocess.run(self.command)
        exit() # opcjonalnie


    def __init__(self):

        root = tk.Tk()
        root.withdraw()

        self.command.append("python3")
        self.command.append("__main__.py")

        self.command.append("-f")
        self.command.append(fd.askopenfilename())

        self.window.title("Wybór algorytmu")
        self.window.geometry("320x320")

        s_box = tk.Checkbutton(self.window,  text="Kolejność domyślna",  variable = self.var_s, onvalue = 1, offvalue = 0)
        p_box = tk.Checkbutton(self.window,  text="Przegląd zupełny",    variable = self.var_p, onvalue = 1, offvalue = 0)
        j_box = tk.Checkbutton(self.window,  text="Reguła Johnsona",     variable = self.var_j, onvalue = 1, offvalue = 0)
        n_box = tk.Checkbutton(self.window,  text="Algorytm Neh",        variable = self.var_n, onvalue = 1, offvalue = 0)
        button = tk.Button(self.window,      text ="Uruchom", command = self.button_interrupt)

        s_box.pack()
        p_box.pack()
        j_box.pack()
        n_box.pack()
        button.pack()

        self.window.mainloop()


gui = Gui()
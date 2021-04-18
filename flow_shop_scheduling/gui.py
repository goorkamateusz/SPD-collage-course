#!/usr/bin/python3
import tkinter as tk
import tkinter.filedialog as fd
import subprocess

class Gui:

    command = []

    var_s = tk.IntVar(0)
    var_p = tk.IntVar(0)
    var_j = tk.IntVar(0)
    var_n = tk.IntVar(0)


    def button_interrupt(self):
        
        if self.var_s.get() == 1:
            self.command.append("-s")

        if self.var_p.get() == 1:
            self.command.append("-p")

        if self.var_j.get() == 1:
            self.command.append("-j")

        if self.var_n.get() == 1:
            self.command.append("-n")        

        subprocess.run(self.command)
        exit() # opcjonalnie


    def __init__(self):

        self.command.append("python3")
        self.command.append("__main__.py")

        self.command.append("-f")
        self.command.append(fd.askopenfilename())


        window = tk.Tk()
        window.title("Wybór algorytmu")
        window.geometry("200x200")


        s_box = tk.Checkbutton(window,  text="Kolejność domyślna",  variable = self.var_s, onvalue = 1, offvalue = 0)
        p_box = tk.Checkbutton(window,  text="Przegląd zupełny",    variable = self.var_p, onvalue = 1, offvalue = 0)
        j_box = tk.Checkbutton(window,  text="Reguła Johnsona",     variable = self.var_j, onvalue = 1, offvalue = 0)
        n_box = tk.Checkbutton(window,  text="Algorytm Neh",        variable = self.var_n, onvalue = 1, offvalue = 0)
        button = tk.Button(window,      text ="Uruchom", command = self.button_interrupt)


        s_box.pack()
        p_box.pack()
        j_box.pack()
        n_box.pack()
        button.pack()

        window.mainloop()


gui = Gui()
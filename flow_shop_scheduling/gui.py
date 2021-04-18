#!/usr/bin/python3
import tkinter as tk
import tkinter.filedialog as fd
import subprocess

class Gui:

    command = []

    var_s = None
    var_p = None
    var_j = None
    var_n = None


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


        window = tk.Tk()
        window.title("Wybór algorytmu")
        window.geometry("200x200")

        self.var_s = tk.IntVar()
        self.var_p = tk.IntVar()
        self.var_j = tk.IntVar()
        self.var_n = tk.IntVar()


        s_box = tk.Checkbutton(window,  text="Kolejność domyślna",  variable = self.var_s)
        p_box = tk.Checkbutton(window,  text="Przegląd zupełny",    variable = self.var_p)
        j_box = tk.Checkbutton(window,  text="Reguła Johnsona",     variable = self.var_j)
        n_box = tk.Checkbutton(window,  text="Algorytm Neh",        variable = self.var_n)
        button = tk.Button(window,      text ="Uruchom", command = self.button_interrupt)


        s_box.pack()
        p_box.pack()
        j_box.pack()
        n_box.pack()
        button.pack()

        window.mainloop()


gui = Gui()
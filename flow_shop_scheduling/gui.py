#!/usr/bin/python3
import tkinter as tk
import tkinter.filedialog as fd
import subprocess
import os
import sys

class Gui:

    command = []
    window = tk.Tk()

    var_s = tk.IntVar()
    var_p = tk.IntVar()
    var_j = tk.IntVar()
    var_n = tk.IntVar()

    var_N = tk.IntVar()
    var_N_track = tk.IntVar()

    def exit_interrupt(self):
        exit()

    def reset_interrupt(self):
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

    def button_interrupt(self):

        if self.var_s.get() == 1:
            self.command.append("-s")

        if self.var_p.get() == 1:
            self.command.append("-p")

        if self.var_j.get() == 1:
            self.command.append("-j")

        if self.var_n.get() == 1:
            self.command.append("-n")   

        if self.var_N.get() == 1:
            self.command.append("-N " + str(self.var_N_track.get()))   

        print(self.command)
        subprocess.run(self.command)

    def __init__(self):

        root = tk.Tk()
        root.withdraw()

        self.command.append("python3")
        self.command.append("__main__.py")

        self.command.append("-f")
        self.command.append(fd.askopenfilename())

        self.window.title("Wybór algorytmu")
        self.window.geometry("640x480")

        s_box = tk.Checkbutton(self.window,  text="Kolejność domyślna",  variable = self.var_s)
        p_box = tk.Checkbutton(self.window,  text="Przegląd zupełny",    variable = self.var_p)
        j_box = tk.Checkbutton(self.window,  text="Reguła Johnsona",     variable = self.var_j)
        n_box = tk.Checkbutton(self.window,  text="Algorytm Neh",        variable = self.var_n)

        N_box = tk.Checkbutton(self.window,  text="Neh zmodyfikowany:",  variable = self.var_N)
        N_trackBar = tk.Scale(self.window, to = 4, variable = self.var_N_track)

        button = tk.Button(self.window,         text ="Uruchom",    command = self.button_interrupt)
        exit_button = tk.Button(self.window,    text ="Wyjście",    command = self.exit_interrupt)
        reset_button = tk.Button(self.window,   text ="Inny plik",  command = self.reset_interrupt)




        reset_button.pack()
        s_box.pack()
        p_box.pack()
        j_box.pack()
        n_box.pack()
        N_box.pack()
        N_trackBar.pack()
        button.pack()
        exit_button.pack()

        self.window.mainloop()


gui = Gui()
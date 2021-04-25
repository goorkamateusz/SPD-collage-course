#!/usr/bin/python3
import tkinter as tk
import tkinter.filedialog as fd
import subprocess
import os
import sys


class Gui:

    command = []
    root = tk.Tk()

    var_s = tk.IntVar()
    var_p = tk.IntVar()
    var_j = tk.IntVar()

    var_t = tk.IntVar()
    var_t_text = tk.Entry(root)

    var_T = tk.IntVar()
    var_T_text = tk.Entry(root)

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

        if self.var_N.get() == 1:
            self.command.append("-N " + str(self.var_N_track.get()))  

        if self.var_t.get() == 1:
            self.command.append("-t " + self.var_t_text.get())

        if self.var_T.get() == 1:
            self.command.append("-T " + self.var_t_text.get() + "," + self.var_T_text.get())

        print(self.command)
        subprocess.run(self.command)
        exit()

    def __init__(self):

        self.command.append("python")
        self.command.append("__main__.py")

        self.command.append("-f")
        self.command.append(fd.askopenfilename())

        self.root.title("Wybór algorytmu")
        self.root.geometry("640x480")

        # CheckBoxy:
        s_box = tk.Checkbutton(self.root,  text="Kolejność domyślna",  variable = self.var_s)
        p_box = tk.Checkbutton(self.root,  text="Przegląd zupełny",    variable = self.var_p)
        j_box = tk.Checkbutton(self.root,  text="Reguła Johnsona",     variable = self.var_j)

        N_box = tk.Checkbutton(self.root,  text="Neh z modyfikacjami:",  variable = self.var_N)
        N_trackBar = tk.Scale(self.root, to = 4, variable = self.var_N_track)

        t_box = tk.Checkbutton(self.root,  text="Tabu search", variable = self.var_t)
        T_box = tk.Checkbutton(self.root,  text="Tabu search z modyfikacjami\nPodaj długość tablicy Tabu powyżej oraz modyfikacje poniżej:", variable = self.var_T)

        # Przyciski:
        button = tk.Button(self.root,         text ="Uruchom",    command = self.button_interrupt)
        exit_button = tk.Button(self.root,    text ="Wyjście",    command = self.exit_interrupt)
        reset_button = tk.Button(self.root,   text ="Inny plik",  command = self.reset_interrupt)

        # Zapakowanie wszystkiego do okna:
        reset_button.pack()

        s_box.pack()
        p_box.pack()
        j_box.pack()

        N_box.pack()
        N_trackBar.pack()

        t_box.pack()
        self.var_t_text.pack()
        T_box.pack()
        self.var_T_text.pack()

        button.pack()
        exit_button.pack()

        self.root.mainloop()


gui = Gui()
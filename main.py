import matplotlib.pyplot as plt
from math import pi
import tkinter as tk
from os.path import basename, splitext
import numpy as np


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Grafárna"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        #amplitudu, fazovy posun, frekvence, počet period, dc složka, nazev grafu?, popisky os?

        self.var_jmeno = tk.StringVar()
        self.var_amplituda = tk.IntVar()
        self.var_faz_posun = tk.IntVar()
        self.var_frekvence = tk.IntVar()
        self.var_periody = tk.IntVar()
        self.var_DC_slozka = tk.IntVar()
        
        #defaultní hodnoty
        self.var_jmeno.set("Mains")
        self.var_amplituda.set(325)
        self.var_faz_posun.set(0)
        self.var_frekvence.set(50)
        self.var_periody.set(2)
        self.var_DC_slozka.set(0)

        vcmd = (self.register(self.callback))
        
        self.lbl_jmeno_grafu = tk.Label(self, text = "Popisek grafu: ")
        self.lbl_jmeno_grafu.grid(row = 1, column = 1, sticky = "w")
        self.entry_jmeno_grafu = tk.Entry(self, width = 30, textvariable = self.var_jmeno)
        self.entry_jmeno_grafu.grid(row = 1, column = 2)

        self.lbl_amplituda = tk.Label(self, text = "Amplituda: ")
        self.lbl_amplituda.grid(row = 2, column = 1, sticky = "w")
        self.entry_amplituda = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_amplituda)
        self.entry_amplituda.grid(row = 2, column = 2)

        self.lbl_faz_posun = tk.Label(self, text = "Fázový posun: ")
        self.lbl_faz_posun.grid(row = 3, column = 1, sticky = "w")
        self.entry_faz_posun = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_faz_posun)
        self.entry_faz_posun.grid(row = 3, column = 2)

        self.lbl_frekvence = tk.Label(self, text = "Frekvence: ")
        self.lbl_frekvence.grid(row = 4, column = 1, sticky = "w")
        self.entry_frekvence = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_frekvence)
        self.entry_frekvence.grid(row = 4, column = 2)
        
        self.lbl_periody = tk.Label(self, text = "Počet period: ")
        self.lbl_periody.grid(row = 5, column = 1, sticky = "w")
        self.entry_periody = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_periody)
        self.entry_periody.grid(row = 5, column = 2)

        self.lbl_DC_slozka = tk.Label(self, text = "DC složka: ")
        self.lbl_DC_slozka.grid(row = 6, column = 1, sticky = "w")
        self.entry_DC_slozka = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_DC_slozka)
        self.entry_DC_slozka.grid(row = 6, column = 2)

        self.btn_vykresli = tk.Button(self, text = "Kreslit", command = self.kresli, width = 10, border = 3, background = "#75d060")
        self.btn_vykresli.grid(row = 7, column = 1)
        
        self.btn_vykresli_example = tk.Button(self, text = "Ze souboru", command = self.load, width = 10, border = 3, background = "#75d060")
        self.btn_vykresli_example.grid(row = 7, column = 2)

        
    def kresli(self):
        jmeno = self.var_jmeno.get()
        amplituda = self.var_amplituda.get()
        faz_posun = self.var_faz_posun.get()
        frekvence = self.var_frekvence.get()
        periody = self.var_periody.get()
        DC_slozka = self.var_DC_slozka.get()
        x = np.linspace(0, periody*1/frekvence, frekvence*10000)
        y = amplituda * (np.sin(2*pi*frekvence*x + np.deg2rad(faz_posun))) + DC_slozka
        plt.plot(x, y, label = jmeno)
        plt.xlabel
        plt.grid(True)
        plt.legend(loc=3)
        plt.show()

    def load(self):
        name = "soubor-win.txt"
        with open(name, "r") as f:
            radky = []
            x = []
            y = []
            i = 0
            while True:
                radek = f.readline()
                radky.append(radek.split())
                if radek == "":
                    break
                x.append(float(radky[i - 1][0]))
                y.append(float(radky[i - 1][1]))
                i = i + 1

        plt.plot(x, y, label = name)
        plt.xlabel
        plt.grid()
        plt.legend()
        plt.show()


    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    

    def quit(self, event = None):
        super().quit()


app = Application()
app.mainloop()




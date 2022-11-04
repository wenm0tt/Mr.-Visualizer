import tkinter as tk
import customtkinter
import matplotlib.pyplot
from matplotlib import *
matplotlib.use('TkAgg')
from sympy import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from copy import copy, deepcopy


class App(customtkinter.CTk):
    WIDTH = 1000
    HEIGHT = 750

    def __init__(self):
        super().__init__()

        self.title("Mr. Visualizer")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  
        
        self.grid_columnconfigure(0)
        self.grid_rowconfigure(1, weight=1)

        self.frame_plot = customtkinter.CTkFrame(master=self,
                                                 width=1000,
                                                 corner_radius=0)
        self.frame_plot.grid(row=1, column=0, sticky="nswe")

        self.frame_control = customtkinter.CTkFrame(master = self, width = 1000, height=150)
        self.frame_control.grid(row=0, column=0, sticky="nswe")


        self.slider_1 = customtkinter.CTkSlider(master=self.frame_control, from_=1, to=20)
        self.slider_1.place(relx = 0.15, rely = 0.5, anchor = tk.CENTER)
        self.slider_1.set(0)

        self.btnPlt = customtkinter.CTkButton(master=self.frame_control,
                                 text="Plot Real",
                                 command=self.plotreal,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
        self.btnPlt.place(relx = 0.85, rely = 0.25, anchor = tk.CENTER)
        self.btnPltComplex = customtkinter.CTkButton(master=self.frame_control,
                                        text="Plot Complex",
                                        command=self.plotcomplex,
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=8)
        self.btnPltComplex.place(relx = 0.7, rely = 0.25, anchor = tk.CENTER)
        self.btnZWPlane = customtkinter.CTkButton(master=self.frame_control,
                                 text="Plot Z Transform",
                                 command=self.animateZW,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
        self.btnZWPlane.place(relx = 0.85, rely = 0.5, anchor = tk.CENTER)
        self.btnPlot3d = customtkinter.CTkButton(master=self.frame_control,
                                        text="Plot 3D",
                                        command=self.animateZW,
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=8)
        self.btnPlot3d.place(relx = 0.7, rely = 0.5, anchor = tk.CENTER)

        self.fig = Figure(figsize=(10,6.5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_plot)
        self.toolbar = NavigationToolbar2Tk(self.canvas,
                                   self.frame_plot)
        self.ax = self.fig.add_subplot(111)

        self.entry = customtkinter.CTkEntry(master=self.frame_control,
                               width=100,
                               height=25, placeholder_text = "Enter Function")
        self.entry.place(relx = 0.4, rely = 0.5, anchor = tk.CENTER)

        self.label_iterations = customtkinter.CTkLabel(text = "Definition and Accuracy", master = self.frame_control) 
        self.label_iterations.place(relx = 0.15, rely = 0.25, anchor = tk.CENTER)
        self.line = matplotlib.pyplot.plot([],[], 'r.')

    def on_closing(self, event = 0):
        self.destroy()

    def plotreal(self):
        self.fig.clear()
        self.ax.axes.clear()
        self.ax = self.fig.add_subplot(111)
        self.toolbar.update()

        x = Symbol('x')
        i = -10
        while i<10:
            if self.entry.get() != "":
                expr = sympify(self.entry.get())
                val = expr.subs(x,i)
                self.ax.plot(i, val, marker = "o",markersize=1, markeredgecolor="red", markerfacecolor="red")
            else:
                raise Exception("pls enter a different function\n           i'm trying my hardest :,( ")
            i += 0.01
    
        self.ax.set_title ("Real Plane", fontsize=16)
        self.ax.set_ylabel("f(x)", fontsize=14)
        self.ax.set_xlabel("x", fontsize=14)
        self.canvas.get_tk_widget().pack(anchor = tk.CENTER)
        self.canvas.draw() 
    
    def plotcomplex(self):
        self.fig.clear()
        self.ax.axes.clear()
        self.ax = self.fig.add_subplot(111, projection = "polar")
        self.toolbar.update()
        x = Symbol('x')
        i = -10
        while i<10:
            if self.entry.get() != "":
                expr = sympify(self.entry.get())
                val = expr.subs(x,i)
                self.ax.plot([0,np.angle(i)],[0,abs(val)],marker='o',markersize=1, markeredgecolor="red", markerfacecolor="red")
            i += 0.01
    
        
        self.ax.set_title ("Complex Plane", fontsize=16)
        self.ax.set_xlabel('                                                 Re')
        self.ax.set_ylabel('                                                 Im')
        self.canvas.get_tk_widget().pack(anchor = tk.CENTER)
        self.canvas.draw() 
    
    def getW(self,x,y):
        expr = self.entry.get()
        cnum = "(" + str(x) + " + " + str(y) + "*I)"
        expr = expr.replace("z", cnum)
        return complex(N(expr))

    def init(self):
        self.line.set_data([],[])
    
        return self.line
    
    def animateZW(self):
        if self.entry.get() == "":
            raise Exception("pls enter a different function\n           i'm trying my hardest :,( ")
        
        for i in range(int(self.slider_1.get())):

            self.fig.clear()
            self.ax.axes.clear()
            self.ax = self.fig.add_subplot(111)
            self.toolbar.update()
            x = np.linspace(-10,10,int(self.slider_1.get()))
            y = np.linspace(-10,10,int(self.slider_1.get()))
            for num in x:
                for anothernum in y:
                    q = self.getW(num,anothernum)
                    matplotlib.pyplot.scatter(q.real, q.imag, marker = ".", c = "#11b5e4")
        
            matplotlib.pyplot.show()
        
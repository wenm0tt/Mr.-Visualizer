import tkinter as tk
import customtkinter
import matplotlib.pyplot
from matplotlib import *
matplotlib.use('TkAgg')
from sympy import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")

def slider_callback(value):
    progressbar_1.set(value)
def printexpr():
    print(entry.get())

app = customtkinter.CTk()
app.geometry("1000x600")
app.title("Newton's Method: A Demonstration")

frame_1 = customtkinter.CTkFrame(master=app, width = 200)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

fig = Figure(figsize=(9,4.5))
canvas = FigureCanvasTkAgg(fig, master=frame_1)
toolbar = NavigationToolbar2Tk(canvas,
                                   frame_1)



progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=12, padx=10)
progressbar_1.set(0)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=12, padx=10)
slider_1.set(0)

def clear(canvas):
    for item in canvas.get_tk_widget().find_all():
       canvas.get_tk_widget().delete(item)

entry = customtkinter.CTkEntry(master=frame_1,
                               width=120,
                               height=25, placeholder_text = "Enter Function")


def plott():
    fig = Figure(figsize=(9,4.5))
    a = fig.add_subplot(111)

    toolbar.update()
    x = Symbol('x')
    i = -10
    while i<10:
        if entry.get() != "":
            expr = sympify(entry.get())
            val = expr.subs(x,i)
            a.plot(i, val, marker = "o",markersize=1, markeredgecolor="red", markerfacecolor="red")
        i += 0.01
   
    
    a.set_title ("Real Plane", fontsize=16)
    a.set_ylabel("f(x)", fontsize=14)
    a.set_xlabel("x", fontsize=14)
    canvas.get_tk_widget().pack()
    canvas.draw() 
    newtall(a)

def newtme(input):
    x = Symbol('x')
    g = input
    for i in range(int(progressbar_1.get()*100)):
        if entry.get() != "":                  
            expr = sympify(entry.get()) 
            val = expr.subs(x,g)
            diffexpr = diff(expr,x)
            diffval = diffexpr.subs(x,g)
        else:
            raise Exception("You must have a function to perform Newton's Method on :(")
        g = g - val/diffval 
        return g

def newtonsmethodbtn():
    newtall()

def plotcomplex():
        fig = Figure(figsize=(9,4.5))
        a = fig.add_subplot(111, projection = "polar")
        toolbar.update()
        a.clear()
        x = Symbol('x')
        i = -10
        while i<10:
            if entry.get() != "":
                expr = sympify(entry.get())
                val = expr.subs(x,i)
                a.plot([0,np.angle(i)],[0,abs(val)],marker='o',markersize=1, markeredgecolor="red", markerfacecolor="red")
            i += 0.01
    
        
        a.set_title ("Complex Plane", fontsize=16)
        a.set_xlabel('                                                 Re')
        a.set_ylabel('                                                 Im')
        canvas.get_tk_widget().pack()
        canvas.draw() 
        newtall(a)
def newtall(ourCanv):
    # x = Symbol('x')
    # if entry.get() == "":
    #     raise Exception("You need a function for me to work on :(")
    # roots = solve(sympify(entry.get()), x)
    # print(roots)

    # i = -10
    # while i < 10:
    #     for element in roots:
    #         if abs(int(element) - newtme(i))< 0.001:
    #             ourCanv.plot(i, 0, marker = "o",markersize=1)
    #     i += 0.1
    pass


btnPlt = customtkinter.CTkButton(master=frame_1,
                                 text="Plot Real",
                                 command=plott,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
btnPlt.place(relx=0.75, rely=0.05, anchor=tk.CENTER)
btnPltNewt = customtkinter.CTkButton(master=frame_1,
                                 text="Newton's Method",
                                 command=newtonsmethodbtn,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
btnPltNewt.place(relx=0.25, rely=0.05, anchor=tk.CENTER)
btnPltComplex = customtkinter.CTkButton(master=frame_1,
                                 text="Plot Complex",
                                 command=plotcomplex,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
btnPltComplex.place(relx = 0.9, rely = 0.05, anchor = tk.CENTER)


entry.place(relx=0.1, rely=0.05, anchor=tk.CENTER)
entry.command = plott

app.mainloop()

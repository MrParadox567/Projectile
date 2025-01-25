import Main_file
import tkinter as tk
import tkinter.messagebox as msg
import math
import turtle

class Pro_Simulate(Main_file.Projectile):
    def __init__(self):
        super().__init__()
        self.bottom_frame = tk.Frame(self.main_window)

        #Making the bottom frame elements
        self.__button = tk.Button(self.bottom_frame,text = "Simulate",
                                  command = self.simulate)
        self.__quit_button = tk.Button(self.bottom_frame,text="Quit",command = self.main_window.destroy)

        #Packing the widgets
        self.__button.pack(side="left")
        self.__quit_button.pack(side="left")

        #Packing the bottom frame
        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def simulate(self):
        theta = math.radians(float(self.angle.get()))
        u = float(self.initial_vel.get())

        g = 9.8

        turtle.bgcolor("RoyalBlue1")
        turtle.pencolor("aquamarine")
        turtle.speed(5)

        for t in range((u**2)*math.sin(2*theta)/g):
            turtle.goto(t*math.tan(theta)-(1/2)*g*(t**2)*((1/(math.cos(theta)))**2)*(1/(u**2)),t)



simulator = Pro_Simulate()









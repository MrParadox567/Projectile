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
        self.theta = math.radians(float(self.angle.get()))
        self.u = float(self.initial_vel.get())

        self.g = 9.8

        turtle.bgcolor("RoyalBlue1")
        turtle.pencolor("aquamarine")
        turtle.speed(5)
        self.Range = (self.u**2)*(math.sin(self.theta*2))/self.g

        for t in range(self.Range):
            turtle.goto(t,t*math.tan(self.theta) - (0.5)*(self.g)*(t**2)*(1/(math.cos(self.theta)**2))*(self.u**2))



simulator = Pro_Simulate()









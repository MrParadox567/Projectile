# this is the main file fo the program
import tkinter as tk
import tkinter.messagebox as msg
import turtle 
import math

class Projectile:
    def __init__(self):
        self.__main_window = tk.Tk()

        #creating frames.
        self.__top_frame = tk.Frame(self.__main_window)
        self.__mid_frame1 = tk.Frame(self.__main_window)
        self.__mid_frame2 = tk.Frame(self.__main_window)

        #Working in the top Frame
        self.__label1 = tk.Label(self.__top_frame,text = "This program simulates the trajectory of a projectile.")
        #Packing the top frame widgets
        self.__label1.pack(side="left")

        #Working in the mid frame1
        self.entrylabel1 = tk.Label(self.__mid_frame1,text = "Enter the Initial Velocity(u) of the projectile:  ")
        self.initial_vel = tk.Entry(self.__mid_frame1,width = 20)
        #Packing the mid frame1 widgets
        self.entrylabel1.pack(side="left")
        self.initial_vel.pack(side="left")

        #Working in the mid_frame2
        self.entrylabel2 = tk.Entry(self.__mid_frame2,text="Enter the value of Angle of projectile: ")
        self.angle = tk.Entry(self.__mid_frame2,width=20)
        #Packing both the widgets
        self.entrylabel2.pack(side="left")
        self.angle.pack(side="left")

        #Packing the frames
        self.__top_frame.pack()
        self.__mid_frame1.pack()
        self.__mid_frame2.pack()

        tk.mainloop()
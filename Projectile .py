import math

class Projectile:
    def __init__(self, initial_velocity, angle):
        self.initial_velocity = initial_velocity
        self.angle = angle
        self.g = 9.81
        self.angle_rad = math.radians(angle)
        self.vx = initial_velocity * math.cos(self.angle_rad)
        self.vy = initial_velocity * math.sin(self.angle_rad)
        self.trajectory = []
    
    def calculate_trajectory(self, time_step=0.1):
        time = 0
        x, y = 0, 0

        while y >= 0:
            self.trajectory.append((x, y))
            time += time_step
            x = self.vx * time
            y = self.vy * time - 0.5 * self.g * time**2
    
    def get_trajectory(self):
        return self.trajectory
      

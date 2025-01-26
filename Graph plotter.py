# Class to handle plotting the trajectory
class Plotter:
    @staticmethod
    def plot_trajectory(trajectory):
        """
        Plots the trajectory of the projectile.
        """
        x_vals, y_vals = zip(*trajectory)  # Separate x and y coordinates
        plt.figure(figsize=(10, 5))
        plt.plot(x_vals, y_vals, label="Projectile Path", color='blue')
        plt.title("Projectile Motion Simulation")
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.legend()
        plt.grid()
        plt.show()


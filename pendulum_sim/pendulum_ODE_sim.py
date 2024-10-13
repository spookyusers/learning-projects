#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:58:16 2024

@author: kym
"""

"""
Find angle of pendulum at time = t.
Call the function theta(t) with whatever time to find the
angle at that time. Change the physical constants to change
initial conditions.

As the variables are set at time of writing, the pendulum
gets extremely close to zero by 5 minutes.

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp

# Physical constants
g = 9.8             # Acceleration due to gravity (m/s^2)
L = 2               # Length of pendulum arm (meters)
mu = 0.1            # Air resistance coefficient

THETA_0 = np.pi / 3 # Initial angle (60 degrees in radians)
THETA_DOT_0 = 0     # Initial angular velocity (rad/s)

# Definition of ODE for the pendulum
def pendulum_ode(t, y):
    theta, theta_dot = y
    theta_double_dot = -mu * theta_dot - (g / L) * np.sin(theta)
    return [theta_dot, theta_double_dot]
    
    
# Solution to the differential equation using solve_ivp
def theta_and_theta_dot(t_max, delta_t=0.01):
    # Time points where the solution is computed
    t_eval = np.arange(0, t_max, delta_t)
    # Initial conditions
    y0 = [THETA_0, THETA_DOT_0]
    # Solve the ODE
    sol = solve_ivp(pendulum_ode, [0, t_max], y0, t_eval=t_eval, method='RK45')
    theta_values = sol.y[0]
    theta_dot_values = sol.y[1]  # Store angular velocity if needed
    return theta_values, theta_dot_values

# Visualization by calculating x and y components
def animate_pendulum(t_max):
    theta_values, theta_dot_values = theta_and_theta_dot(t_max)
    x_vals = L * np.sin(theta_values)
    y_vals = -L * np.cos(theta_values)

    fig, ax = plt.subplots()
    ax.set_xlim(-L - 0.1, L + 0.1)
    ax.set_ylim(-L - 0.1, 0.1)
    ax.set_aspect('equal')  # Ensure the aspect ratio is equal
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    def init():
        """Initialize the background of the animation."""
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text

    def update(i):
        """Update the animation by setting new data."""
        x = [0, x_vals[i]]
        y = [0, y_vals[i]]
        line.set_data(x, y)
        time_text.set_text(f'Time = {i * 0.01:.2f}s')
        return line, time_text

    ani = animation.FuncAnimation(
            fig, update, frames=len(theta_values),
            init_func=init, blit=True, interval=10
    )

    plt.show()

# Simulate and animate the pendulum for 10 seconds
if __name__ == "__main__":
    animate_pendulum(30)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:58:16 2024

@author: kym
"""

"""
Simulate and animate a mass-spring system.
Call the function x(t) with whatever time to find the
displacement at that time. Change the physical constants to change
initial conditions.

As the variables are set at time of writing, the mass oscillates and gradually
comes to rest due to damping.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp

# Physical constants
m = 0.5          # Mass (kg)
k = 22.206         # Spring constant (N/m)
b = 0.4626          # Damping coefficient (kg/s)

X0 = 0.0005         # Initial displacement (meters)

V0 = 0.0         # Initial velocity (m/s)

# Definition of ODE for the mass-spring system
def mass_spring_ode(t, y):
    x, v = y
    # Newton's second law: m*x'' + b*x' + k*x = 0
    x_double_dot = (-b * v - k * x) / m
    return [v, x_double_dot]

# Solution to the differential equation using solve_ivp
def displacement_and_velocity(t_max, delta_t=0.01):
    # Time points where the solution is computed
    t_eval = np.arange(0, t_max, delta_t)
    # Initial conditions
    y0 = [X0, V0]
    # Solve the ODE
    sol = solve_ivp(mass_spring_ode, [0, t_max], y0, t_eval=t_eval, method='RK45')
    x_values = sol.y[0]
    v_values = sol.y[1]  # Store velocity if needed
    return x_values, v_values

# Visualization by calculating positions
def animate_mass_spring(t_max):
    x_values, v_values = displacement_and_velocity(t_max)
    
    # Parameters for visualization
    spring_rest_length = 1.0  # Rest length of the spring (meters)
    mass_radius = 0.2         # Radius of the mass (for visualization)
    num_coils = 20            # Number of coils in the spring
    coil_amplitude = 0.1      # Horizontal amplitude of coils
    
    # Initialize the figure and axis
    fig, ax = plt.subplots()
    
    # Determine y-axis limits based on maximum displacement
    max_displacement = np.max(np.abs(x_values)) + spring_rest_length
    y_min = -0.5  # Some space above the fixed point
    y_max = spring_rest_length + max_displacement + 0.5  # Space below for mass movement
    ax.set_xlim(-coil_amplitude * 2, coil_amplitude * 2)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect('equal')  # Ensure the aspect ratio is equal
    ax.grid()
    
    # Initialize spring as a line and mass as a circle
    spring_line, = ax.plot([], [], 'b-', lw=2)
    mass = plt.Circle((0, 0), mass_radius, fc='r', ec='k')
    ax.add_patch(mass)
    time_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12)
    
    def init():
        """Initialize the background of the animation."""
        spring_line.set_data([], [])
        mass.center = (0, spring_rest_length)
        time_text.set_text('')
        return spring_line, mass, time_text
    
    def update(i):
        """Update the animation by setting new data."""
        # Current displacement
        x = x_values[i]
        
        # Current spring length
        current_length = spring_rest_length + x
        
        # Create spring coils
        coil_spacing = current_length / num_coils
        y = np.linspace(0, current_length, num_coils + 1)
        x_coil = coil_amplitude * np.sin(2 * np.pi * np.linspace(0, 1, num_coils + 1))
        
        # Fixed top position
        x_top, y_top = 0, 0
        
        # Moving bottom position
        x_bottom, y_bottom = 0, current_length
        
        # Combine top and coils
        x_spring = x_coil
        y_spring = y
        
        # Update spring line
        spring_line.set_data(x_spring, y_spring)
        
        # Update mass position (center of the mass)
        mass.center = (x_spring[-1], y_spring[-1])
        
        # Update time text
        time_text.set_text(f'Time = {i * 0.01:.2f}s')
        
        return spring_line, mass, time_text
    
    ani = animation.FuncAnimation(
            fig, update, frames=len(x_values),
            init_func=init, blit=True, interval=10, repeat=False
    )
    
    plt.title('Mass-Spring System Animation')
    plt.xlabel('Horizontal Position (m)')
    plt.ylabel('Vertical Position (m)')
    plt.show()

# Simulate and animate the mass-spring system for 10 seconds
if __name__ == "__main__":
    animate_mass_spring(10)

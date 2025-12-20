import numpy as np
import matplotlib.pyplot as plt
import textwrap

# Constants
h = 6.62607015e-34      # J s
c = 2.99792458e8        # m/s
k = 1.380649e-23        # J/K
T = 5700                # K (Sun temperature)
procyon = 6400
sirius = 9200
betelgeuse = 3400

# wavelength array in micrometers -> convert to meters
u = np.linspace(0.01, 30.0, 2000)   
# micrometers (start from 0.01 to avoid division issues)
# creates an array of 2000 values between 0.01 and 30.0. These are our points on the x-axis.
# u = wavelength in micrometers

lam = u * 1e-6                      # converts micrometers to meters

# Planck function (energy density per unit wavelength)
planck = (8*np.pi*h*c) / (lam**5 * (np.exp(h*c/(lam*k*T)) - 1))
plankProcyon = (8*np.pi*h*c) / (lam**5 * (np.exp(h*c/(lam*k*procyon)) - 1))
plankSirius = (8*np.pi*h*c) / (lam**5 * (np.exp(h*c/(lam*k*sirius)) - 1))
plankBetelgeuse = (8*np.pi*h*c) / (lam**5 * (np.exp(h*c/(lam*k*betelgeuse)) - 1))

# Rayleigh-Jeans approximation
rj = (8*np.pi*k*T) / (lam**4)

# Plot 1: Wavelength range 0-30 μm
plt.figure(figsize=(10, 6)) # creates screen size (width, height)
plt.plot(u, planck, 'k-', label="Planck's Law (Sun)", linewidth=1.5) # plots the planck function
plt.plot(u, rj, 'r--', label="Rayleigh-Jeans Law (Sun)", linewidth=1.5) # plots the rayleigh-jeans function
plt.xlabel('Wavelength (micrometers)', fontsize=12)
plt.ylabel('Energy Density: f(λ)', fontsize=12)
plt.xlim(0, 30) # sets the x-axis range
plt.ylim(0, 300) # sets the y-axis range
plt.title('Graph #1: Blackbody Radiation', fontsize=14, fontweight='bold')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.5)
plt.tight_layout(rect=[0, 0.08, 1, 1])
wrapped_text = textwrap.fill('Comparison of Planck\'s Law and Rayleigh-Jeans Law for the Sun (T=5700K) over larger wavelengths. You can see that at large wavelength, Plank\'s Law and Rayleigh-Jeans Law are fairly equal.',
                            width=80)
plt.figtext(0.5, 0.02, wrapped_text, ha='center', fontsize=10, style='italic')
plt.show()

# Plot 2: Wavelength range 0-4 μm
plt.figure(figsize=(10, 6))
plt.plot(u[u <= 4], planck[u <= 4], 'k-', label="Planck's Law (Sun)", linewidth=1.5)
plt.plot(u[u <= 4], rj[u <= 4], 'r--', label="Rayleigh-Jeans Law (Sun)", linewidth=1.5)
plt.xlabel('Wavelength (micrometers)', fontsize=12)
plt.ylabel('Energy Density: f(λ)', fontsize=12)
plt.xlim(0, 4)
plt.ylim(0, 2000000)
plt.title('Graph #2: Blackbody Radiation', fontsize=14, fontweight='bold')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.5)
plt.tight_layout(rect=[0, 0.08, 1, 1])
wrapped_text = textwrap.fill('Zoomed out view showing divergence between Planck\'s Law and Rayleigh-Jeans Law at shorter wavelengths. Proving the \'ultraviolet catastrophe\'.', 
                            width=80)
plt.figtext(0.5, 0.02, wrapped_text, ha='center', fontsize=10, style='italic')
plt.show()

# Plot 3: 
plt.figure(figsize=(10, 6))
plt.plot(u[u <= 4], planck[u <= 4], 'k-', label="Planck's Law (Sun T = 5700K)", linewidth=1.5)
plt.plot(u[u <= 4], plankProcyon[u <= 4], 'k--', label="Planck's Law (Procyon T = 6400K)", linewidth=1.5)
plt.plot(u[u <= 4], plankSirius[u <= 4], 'b-', label="Planck's Law (Sirius T = 9200K)", linewidth=1.5)
plt.plot(u[u <= 4], plankBetelgeuse[u <= 4], 'r-', label="Planck's Law (Betelgeuse T = 3400K)", linewidth=1.5)
plt.xlabel('Wavelength (micrometers)', fontsize=12)
plt.ylabel('Energy Density: f(λ)', fontsize=12)
plt.xlim(0, 2)
plt.ylim(0, 12000000)
plt.title('Graph #3: Blackbody Radiation of The Sun, Procyon, Sirius, and Betelgeuse', fontsize=14, fontweight='bold')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.5)
plt.tight_layout(rect=[0, 0.08, 1, 1])
wrapped_text = textwrap.fill('Comparison of energy emission for stars at different temperatures. Higher temperature stars emmit more energy and peak at shorter wavelengths. This is why Sirius is blue and Betelgeuse is red.', 
                             width=80)
plt.figtext(0.5, 0.02, wrapped_text, ha='center', fontsize=10, style='italic')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(u[u <= 4], planck[u <= 4], 'k-', label="Planck's Law (Sun T = 5700K)", linewidth=1.5)
plt.plot(u[u <= 4], plankBetelgeuse[u <= 4], 'r-', label="Planck's Law (Betelgeuse T = 3400K)", linewidth=1.5)
plt.xlabel('Wavelength (micrometers)', fontsize=12)
plt.ylabel('Energy Density: f(λ)', fontsize=12)
plt.xlim(0, 2)
plt.ylim(0, 1100000)
plt.title('Graph #4: Blackbody Radiation of The Sun and Betelgeuse (zoomed in)', fontsize=14, fontweight='bold')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.5)
plt.tight_layout(rect=[0, 0.08, 1, 1])
wrapped_text = textwrap.fill('Zoomed in comparison showing the Sun vs Betelgeuse. Betelgeuse is cooler and emits most of its energy at longer wavelengths making it redder.', 
                             width=80)
plt.figtext(0.5, 0.02, wrapped_text, ha='center', fontsize=10, style='italic')
plt.show()
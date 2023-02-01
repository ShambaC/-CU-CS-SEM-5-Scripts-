# Find the modulus and phase angle of a complex number in python.

import cmath

# Init
x = int(input('Enter real part : '))
y = int(input('Enter complex part : '))
z = complex(x, y)

print(f"Given complex number is : {z}")
print(f"Real part is : {z.real}")
print(f"Imaginary part is : {z.imag}")

# Modulus
mod_val = abs(z)
print(f"Mod value of {z} is : {mod_val}")

# Phase
phase_val = cmath.phase(z)
print(f"Phase of {z} is : {phase_val}")
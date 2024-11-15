import numpy as np
import matplotlib.pyplot as plt

# Define the sine wave parameters
frequency = 1  # Frequency in Hz
amplitude = 1  # Amplitude of the wave
time = np.linspace(0, 1, 500)  # Time vector

# Generate the sine wave stuff
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

# Plot the sine wave
plt.plot(time, sine_wave)
plt.title("Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
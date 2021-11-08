import time
import math

LEFT = "-"
RIGHT = "="
LEN = 21
PERIOD = 30

def wave_length(count):
    current_length = LEN + LEN * math.sin(2 * math.pi * (count / PERIOD))
    return current_length

def wave(wavelength):
    left_size = int(round(wavelength))
    print((LEFT * left_size) + (RIGHT * (2 * LEN - left_size)))
    time.sleep(0.1)

if __name__ == "__main__":
    for i in range(PERIOD * 100):
        wave(wave_length(i))

from math import pi, cos
import os
from time import sleep

def circle(x, y):
    return x ** 2 + y ** 2 <= 100

def parabola(x, y):
    return x ** 2 < y

def heart(x, y):
    a = 12
    b = 10
    y = y / b
    x = x / a
    return (y - ((x ** 2) ** (1/3))) ** 2 + x ** 2 <= 1

a = 17
b = 17
def butterfly(x, y):
    x = x / a
    y = y / b
    in_left = (x + 1) ** 2 + y ** 2 <= 1 \
        and abs(5 * y) + x >= -0.3 \
        and (x + 5.7) ** 2 + (y + 1) ** 2 >= 25
    in_right = (x - 1) ** 2 + y ** 2 <=1 \
        and abs(5 * y) - x >= -0.3 \
        and (x - 5.7) ** 2 + (y + 1) ** 2 >= 25
    return in_left or in_right

def vertex_score(f, x, y):
    total = 0
    total += int(f(x, y))
    total += 2 * int(f(x + 1, y))
    total += 4 * int(f(x, y - 1))
    total += 8 * int(f(x + 1, y - 1))
    total += 16 * int(f(x, y - 2))
    total += 32 * int(f(x + 1, y - 2))
    return total

# this could be an array, but this is easier to read while debugging
score_to_char = {
    0: ' ',
    1: '\'',
    2: '`',
    3: '^',
    4: ' ',
    5: '\'',
    6: '\'',
    7: '\'',
    8: ' ',
    9: '`',
    10: '\'',
    11: '\'',
    12: '=',
    13: '*',
    14: '*',
    15: '*',
    16: ',',
    17: ':',
    18: '/',
    19: '\'',
    20: ',',
    21: '[',
    22: '[',
    23: '7',
    24: ',',
    25: ')',
    26: ':',
    27: ':',
    28: 'r',
    29: 'D',
    30: '/',
    31: 'P',
    32: '.',
    33: '\\',
    34: ':',
    35: ':',
    36: '.',
    37: ':',
    38: '(',
    39: 'C',
    40: '.',
    41: ':',
    42: ']',
    43: ']',
    44: 'v',
    45: '\\',
    46: 'G',
    47: '4',
    48: '.',
    49: ';',
    50: ':',
    51: ':',
    52: 'u',
    53: 'L',
    54: 'C',
    55: 'C',
    56: 'u',
    57: 'u',
    58: ']',
    59: ']',
    60: 'm',
    61: 'b',
    62: 'd',
    63: 'M',
}

width = 40
height = 40
x_offset = -20
y_offset = -20

# ascii characters are roughly twice as tall as they are wide
# so we should halve the step size of x (but we cant)
# so instead we double the step size of y
# - we must account for this when calculating a vertex score
theta = 0
dtheta = 2 * pi / 41
initial_a = a
for _ in range(1000):
    os.system("clear")
    for j in range(height + y_offset, y_offset, -2):
        for i in range(x_offset, width + x_offset):
            print(score_to_char[vertex_score(butterfly, i, j)], end="")

        print()

    theta += dtheta
    a = initial_a * cos(theta)
    sleep(1/12)
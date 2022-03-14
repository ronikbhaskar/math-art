"""
These are all functions that take an x and a y, and output a boolean value
Can be used to draw two-color images
"""

import PIL.Image
from math import floor

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

def butterfly(x, y):
    a = 17
    b = 17
    x = x / a
    y = y / b
    in_left = (x + 1) ** 2 + y ** 2 <= 1 \
        and abs(5 * y) + x >= -0.3 \
        and (x + 5.7) ** 2 + (y + 1) ** 2 >= 25
    in_right = (x - 1) ** 2 + y ** 2 <=1 \
        and abs(5 * y) - x >= -0.3 \
        and (x - 5.7) ** 2 + (y + 1) ** 2 >= 25
    return in_left or in_right

def resize_image(image, max_dim):
    width, height = image.size
    if width < height:
        width = floor(max_dim * width / height)
        height = max_dim
    else:
        height = floor(max_dim * height / width)
        width = max_dim
    
    return image.resize((width, height))

def image_to_function(path_to_image, max_dim = 10):
    """
    returns a function for the given image for ascii conversion
    """
    image = PIL.Image.open(path_to_image)
    image = resize_image(image, max_dim)
    width, height = image.size
    pixels = image.getdata()
    
    def image_to_bool(x, y):
        if not (0 <= x < width and 0 <= y < height):
            return False
        elif pixels[x + (height - y - 1) * width][3] > 50:
            return True
        return False

    return image_to_bool
    


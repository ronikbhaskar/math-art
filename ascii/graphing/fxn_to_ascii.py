
from R2_to_bool import circle, parabola, heart, butterfly, image_to_function

def vertex_score(f, x, y):
    """
    takes six points and combines them to understand which points in a region are covered
    output is value 0 to 63 inclusive
    """
    total = 0
    total += int(f(x, y))
    total += 2 * int(f(x + 1, y))
    total += 4 * int(f(x, y - 1))
    total += 8 * int(f(x + 1, y - 1))
    total += 16 * int(f(x, y - 2))
    total += 32 * int(f(x + 1, y - 2))
    return total

# takes index 0 to 63, outputs a one-character string
# technically not a character because we don't have 8-bit types
SCORE_TO_CHAR = [
    ' ',
    '\'',
    '`',
    '^',
    ' ',
    '\'',
    '\'',
    '\'',
    ' ',
    '`',
    '\'',
    '\'',
    '=',
    '*',
    '*',
    '*',
    ',',
    ':',
    '/',
    '\'',
    ',',
    '[',
    '[',
    '7',
    ',',
    ')',
    ':',
    ':',
    'r',
    'D',
    '/',
    'P',
    '.',
    '\\',
    ':',
    ':',
    '.',
    ':',
    '(',
    'C',
    '.',
    ':',
    ']',
    ']',
    'v',
    '\\',
    'G',
    '4',
    '.',
    ';',
    ':',
    ':',
    'u',
    'L',
    'C',
    'C',
    'u',
    'u',
    ']',
    ']',
    'm',
    'b',
    'd',
    'M',
]

def function_to_ascii(f, width, height, x_offset, y_offset):
    """
    f should take x and y and output bool 
    width: unit width of grid
    height: unit height of grid
    x_offset: min x as int
    y_offset: min y as int
    """

    # ascii characters are roughly twice as tall as they are wide
    # so we should halve the step size of x (but we cant)
    # so instead we double the step size of y
    # - we must account for this when calculating a vertex score

    for j in range(height + y_offset, y_offset, -2):
        for i in range(x_offset, width + x_offset):
            print(SCORE_TO_CHAR[vertex_score(f, i, j)], end="")

        print()

def main():
    function_to_ascii(heart, 40, 40, -20, -20)

if __name__ == "__main__":
    main()
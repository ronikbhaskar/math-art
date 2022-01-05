
import os
import random
import time
import copy

BKG_FILE = "bkg.txt"

def get_screen(width, height):
    with open(BKG_FILE) as f:
            bkg = f.readlines()

    screen = [" " * width] * height

    bkg_height = len(bkg)

    for i, bkg_row in enumerate(bkg):
        bkg_row_len = len(bkg_row)
        screen[height + i - bkg_height] = bkg_row[:-1] + " " * (width - bkg_row_len + 1)

    return screen

def get_snow(width, height, num_flakes):
    patterns = [".","+","*"]

    flakes = [[random.choice(patterns), 
               random.randint(0,width - 1), 
               random.randint(0,height - 1)] 
              for _ in range(num_flakes)]

    return flakes

def animate(width, height, screen, snow, iter=100):

    for i in range(iter):
        display = copy.deepcopy(screen)
        for flake in snow:
            display[flake[2]] = display[flake[2]][:flake[1]] + flake[0] + display[flake[2]][flake[1] + 1:]
            if not i % 2:
                continue

            if random.random() < 0.9:
                flake[2] = (flake[2] + 1) % height

            rand = random.random()
            if rand < 0.1:
                flake[1] = (flake[1] + 1) % width
            elif rand < 0.2:
                flake[1] = (flake[1] - 1) % width
            
        time.sleep(0.1)
        os.system("clear")
        for row in display:
            print(row)


def main():
    width, height = os.get_terminal_size()
    screen = get_screen(width, height)
    snow = get_snow(width, height, 10)
    
    animate(width, height, screen, snow, iter = 1000)

if __name__ == "__main__":
    main()
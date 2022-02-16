import time
import math
from random import randint
import os
from datetime import datetime, timezone
import getopt
import sys

class Sky():
    """
    overarching class for the night sky animation
    """

    def __init__(self, width, height):
        """
        width : int
        height : int
        constructs a board of strings filled with spaces
        initializes the frame to 0
        sets the framerate to 0.1s
        """

        self.width = width
        self.height = height
        self.board = [" " * width for _ in range(height)]
        self.frame = 0
        self.celestials = []
        self.framerate_recip = 0.1

    def add(self, celestial):
        """
        appends the celestial body to the list
        """

        self.celestials.append(celestial)

    def update(self):
        """
        standard update function for animation
        """

        self.frame += 1
        for celestial in self.celestials:
            celestial.update(self.frame)

    def clear(self):
        """
        clears the board
        """

        self.board = [" " * self.width for _ in range(self.height)]

    def draw(self):
        """
        standard draw function for animation
        """

        print("\033[2J")
        self.clear()
        for celestial in self.celestials:
            # self.board = celestial.draw(self.board)
            celestial.draw(self.board)
        for line in self.board:
            print(line)

    def run(self, frames):
        """
        imprecise run function for ascii animation of Sky
        """

        while self.frame <= frames: 
            self.draw()
            self.update()
            time.sleep(self.framerate_recip)

        self.frame = 0

class Celestial():
    """
    "abstract" Celestial class for use in Sky
    back to OOP
    """

    def __init__(self, x, y, width, height, drawings):
        """
        x : int
        y : int
        width : int
        height : int
        drawing : List[List[str]]
        """
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.drawings = drawings
        self.num_frames = len(drawings)
        self.current_drawing = drawings[0]

    def update(self,frame):
        """
        reusable update function
        """

        frame %= self.num_frames # technically not necessary
        self.current_drawing = self.drawings[frame]

    def draw(self, board):
        """
        returns updated version of the board
        """

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if (0 <= i - self.y < self.height) and (0 <= j - self.x < self.width):
                    new_char = self.current_drawing[i - self.y][j - self.x]
                    board[i] = board[i][0:j] + new_char + board[i][j+1:]

class DimStar(Celestial):

    DRAWINGS = [["."]]
    WIDTH, HEIGHT = 1, 1

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         DimStar.WIDTH, 
                         DimStar.HEIGHT, 
                         DimStar.DRAWINGS)

class BrightStar(Celestial):

    DRAWINGS = [["*"]]
    WIDTH, HEIGHT = 1, 1

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         BrightStar.WIDTH, 
                         BrightStar.HEIGHT, 
                         BrightStar.DRAWINGS)
    
class BrightStarVariant(Celestial):

    DRAWINGS = [["+"]]
    WIDTH, HEIGHT = 1, 1

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         BrightStarVariant.WIDTH, 
                         BrightStarVariant.HEIGHT, 
                         BrightStarVariant.DRAWINGS)
    
class BigPlanet(Celestial):

    DRAWINGS = [["O"]]
    WIDTH, HEIGHT = 1, 1

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         BigPlanet.WIDTH, 
                         BigPlanet.HEIGHT, 
                         BigPlanet.DRAWINGS)
    
class SmallPlanet(Celestial):

    DRAWINGS = [["ø"]]
    WIDTH, HEIGHT = 1, 1

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         SmallPlanet.WIDTH, 
                         SmallPlanet.HEIGHT, 
                         SmallPlanet.DRAWINGS)
    
class TwinklingStar(Celestial):

    DRAWINGS = [["-"],["|"]]
    WIDTH, HEIGHT = 1, 1

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         TwinklingStar.WIDTH, 
                         TwinklingStar.HEIGHT, 
                         TwinklingStar.DRAWINGS)

class FullMoon(Celestial):

    DRAWINGS = [["  ,----.  ",
                " / o __\\\ ",
                "| \_/   O|",
                " \ .    / ",
                "  `----\"  "]]
    WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         FullMoon.WIDTH, 
                         FullMoon.HEIGHT, 
                         FullMoon.DRAWINGS)
    
class FirstQuarterMoon(Celestial):

    DRAWINGS = [["     --.  ",
                 "     |_\\\ ",
                 "     |  O|",
                 "     |  / ",
                 "     --\"  "]]
    WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         FirstQuarterMoon.WIDTH, 
                         FirstQuarterMoon.HEIGHT, 
                         FirstQuarterMoon.DRAWINGS)
    
class LastQuarterMoon(Celestial):

    DRAWINGS = [["  ,--     ",
                 " / o|     ",
                 "| \_/     ",
                 " \ .|     ",
                 "  `--     "]]
    WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         LastQuarterMoon.WIDTH, 
                         LastQuarterMoon.HEIGHT, 
                         LastQuarterMoon.DRAWINGS)

class NewMoon(Celestial):

    DRAWINGS = [["          ",
                 "          ",
                 "          ",
                 "          ",
                 "          ",]]
    WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         NewMoon.WIDTH, 
                         NewMoon.HEIGHT, 
                         NewMoon.DRAWINGS)
  
class Meteor(Celestial):

    def _generate_drawings(seed):
        blank = ["    ",
                "    ",
                "    ",
                "    "]
        frame_1 = ["    ",
                  "    ",
                  "    ",
                  "o   "]
        frame_2 = ["    ",
                  "    ",
                  " o  ",
                  "/   "]
        frame_3 = ["    ",
                  "  o ",
                  " /  ",
                  "/   "]
        frame_4 = ["   o",
                  "  / ",
                  " /  ",
                  "    "]
        frame_5 = ["   /",
                  "  / ",
                  "    ",
                  "    "]
        frame_6 = ["   /",
                  "    ",
                  "    ",
                  "    "]
        
        drawings = [blank for _ in range(seed)]
        drawings.append(frame_1)
        drawings.append(frame_2)
        drawings.append(frame_3)
        drawings.append(frame_4)
        drawings.append(frame_5)
        drawings.append(frame_6)
        return drawings

    # DRAWINGS = _generate_drawings()
    WIDTH, HEIGHT = 4, 4

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         Meteor.WIDTH, 
                         Meteor.HEIGHT, 
                         Meteor._generate_drawings(randint(20,40)))

def get_moon_phase():
    # I want to use integers, so
    # period ~ 29.53059 days
    # period * 100000 * 86400 s / day -> 
    # period = 255144297600 # s / 100000 <- units
    # dividing the period of the moon into 4 segments,
    # phase_len = 63786074400 s / 100000
    # to convert to ms, we multiply by 100
    # because 1 / 100000 * 100 = 1 / 1000, so
    phase_len_ms = 637860744
    harvest_moon_2021 = datetime(2021, 9, 20, 23, 55, tzinfo=timezone.utc)
    dt_now = datetime.now(tz=timezone.utc)
    diff_ms = round((dt_now - harvest_moon_2021).total_seconds() * 1000)
    # I know you shouldn't round multiple times in general when
    # approximating a value, but I want to make sure the division
    # is done with integers, since there is no maximum
    # (long) integer size in Python
    phase = round(diff_ms / phase_len_ms) % 4
    return phase

def usage():
    """
    prints simple usage information
    """

    print("\nSTARS.PY")
    print("args:")
    print("-p {phase} : optional, changes phase of moon, takes val 0-3")
    print("\talias --phase")
    print("\t0 : new moon")
    print("\t1 : first quarter")
    print("\t2 : full moon")
    print("\t3 : last quarter")
    print("\tdefault is the actual moon phase\n")
    print("-t {phase} : optional, int between 0 and 10000, sets number of frames")
    print("\talias --time")
    print("\tdefaults to 10000\n")
    print("-h : prints usage information")
    print("\talias --help\n")

def str_to_int_in_range(opt, arg, min, max):
    """
    converts string to int, min <= x < max
    exits if fail (for use in arg parsing)
    """

    msg = f"{opt} takes an integer between {min} and {max - 1}"

    try:
        arg = int(arg)
    except ValueError as err:
        print(msg)
        sys.exit(1)

    if arg < min or arg >= max:
        print(msg)
        sys.exit(1)

    return arg


def main():
    # C-style arg parse bc I want to 
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:p:h", ["time=","phase=","help"])
    except getopt.GetoptError as err:
        # print usage information and exit:
        print(err) # option arg not recognized
        usage()
        sys.exit(1)
    
    phase = get_moon_phase()
    time = 10000

    for opt, arg in opts:
        if opt in ("-p", "--phase"):
            arg = str_to_int_in_range(opt, arg, 0, 4)
            phase = (arg + 2) % 4
        elif opt in ("-t", "--time"):
            arg = str_to_int_in_range(opt, arg, 0, 10001)
            time = arg
        elif opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        else:
            input(f"Unhandled option {arg}. Press ENTER to continue anyways")

    # finished parsing args

    moon_phases = [FullMoon, LastQuarterMoon, NewMoon, FirstQuarterMoon]
    Moon = moon_phases[phase]
    os.system("clear")
    width, height = 80, 20
    sky = Sky(width, height)
    
    for i in range(3):
        sky.add(DimStar(randint(0,width),randint(0,height))) 
        sky.add(BrightStar(randint(0,width),randint(0,height)))
        sky.add(BrightStarVariant(randint(0,width),randint(0,height)))
        # sky.add(TwinklingStar(randint(0,width),randint(0,height)))
    
    sky.add(Moon(14,0))
    # To change this to a different moon phase,
    # use arg -p with 0 for new moon, 1 for first quarter, 2 for full, 3 for last
    sky.add(BigPlanet(55,6))
    sky.add(SmallPlanet(75,10))
    sky.add(Meteor(0,0))
    sky.add(Meteor(3,3))
    sky.add(Meteor(37,4))
    sky.add(Meteor(41,8))
    sky.add(Meteor(41,3))
    sky.run(time)

if __name__ == "__main__":
    main()
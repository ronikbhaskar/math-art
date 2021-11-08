import time
import math
from random import randint
import os

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
                "  `--"]]
    WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y):
        super().__init__(x, 
                         y, 
                         LastQuarterMoon.WIDTH, 
                         LastQuarterMoon.HEIGHT, 
                         LastQuarterMoon.DRAWINGS)
  
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

if __name__ == "__main__":
    os.system("clear")
    width, height = 80, 20
    sky = Sky(width, height)
    
    for i in range(3):
        sky.add(DimStar(randint(0,width),randint(0,height))) 
        sky.add(BrightStar(randint(0,width),randint(0,height)))
        sky.add(BrightStarVariant(randint(0,width),randint(0,height)))
        # sky.add(TwinklingStar(randint(0,width),randint(0,height)))
    
    sky.add(FirstQuarterMoon(14,0))
    # To change this to a different moon phase,
    # replace FirstQuarterMoon with LastQuarterMoon or FullMoon.
    sky.add(BigPlanet(55,6))
    sky.add(SmallPlanet(75,10))
    sky.add(Meteor(0,0))
    sky.add(Meteor(3,3))
    sky.add(Meteor(37,4))
    sky.add(Meteor(41,8))
    sky.add(Meteor(41,3))
    sky.run(10000)


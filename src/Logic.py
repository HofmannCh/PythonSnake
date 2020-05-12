from models.Grid import Grid
from time import sleep
import random

class Logic:
    def __init__(self):
        self.sizeY = 24
        self.sizeX = 24
        self.grid = Grid(self.sizeY, self.sizeX)
        
        # random.seed(123)

        self.isRunning = False
        self.__internalStop = False
        self.reset()

    def getRandomApplePos(self):
        while True:
            y = random.randint(0, self.sizeY-1)
            x = random.randint(0, self.sizeX-1)
            t = self.grid.getTiles2D()[y][x]
            if(not t.isSnake):
                return t

    def onDirectionChange(self, direction):
        self.direction = direction

    def reset(self):
        if(self.isRunning):
            self.__internalStop = True
            return

        print("Reset")

        for t in self.grid.getTiles1D():
            t.setState(None)

        # the beginning of the array is the head (index 0) and the end is the tail
        # the first four pices of the grid is the starter snake (::-1 is that the head of the snake is looking into the field and not to the wall at 0 0)
        self.snake = self.grid.getTiles1D()[0:4][::-1]

        for s in self.snake:
            s.setState("s")
        self.apple = self.getRandomApplePos()
        self.apple.setState("a")
        self.countApple = 0
        self.iter = 0

        self.direction = "r"
        self.lastDirection = "r"        

    def getGrid(self):
        return self.grid

    def loop(self):
        # internal stop
        if(self.__internalStop):
            self.__internalStop = False
            self.isRunning = False
            self.reset()
            return False
        
        # direction
        if(self.lastDirection == "u" and self.direction == "d"):
            self.direction = self.lastDirection
        elif(self.lastDirection == "r" and self.direction == "l"):
            self.direction = self.lastDirection
        elif(self.lastDirection == "d" and self.direction == "u"):
            self.direction = self.lastDirection
        elif(self.lastDirection == "l" and self.direction == "r"):
            self.direction = self.lastDirection
        self.lastDirection = self.direction

        # evaluate next snake field
        st = self.snake[0].getDirection(self.direction)
        self.isRunning = not st == None
        if(not self.isRunning or st.isSnake):
            self.__internalStop = False
            self.isRunning = False
            self.reset()
            return False
        
        # check if apple
        if(st == self.apple):
            self.countApple += 1
            print(self.countApple)
            self.apple = self.getRandomApplePos()
            self.apple.setState("a")
        else:
            # if not apple then remove one pice from snake tail
            self.snake.pop().setState(None)

        st.setState("s")
        self.snake.insert(0, st) # insert at head

        self.iter += 1
        return True

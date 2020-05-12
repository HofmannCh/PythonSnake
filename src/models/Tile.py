class Tile:
    def __init__(self, y, x, grid):
        self.y = y
        self.x = x
        self.grid = grid

        self.isSnake = False
        self.isApple = False

    def setState(self, s):
        if(s == None): s = ""
        self.isSnake = s.lower() == "s"
        self.isApple = s.lower() == "a"

    def getKey(self):
        return self.__str__()

    def getDirection(self, direction):
        math = None

        if(direction == "l"):
            math = (0, -1)
        elif(direction == "u"):
            math = (-1, 0)
        elif(direction == "r"):
            math = (0, 1)
        elif(direction == "d"):
            math = (1, 0)
        
        if(math == None): return None

        tiles = self.grid.getTiles2D()

        ny = self.y + math[0]
        nx = self.x + math[1]


        if(ny >= 0 and nx >= 0 and ny < len(tiles) and nx < len(tiles[ny])):
            return tiles[ny][nx]

        return None

    def __str__(self):
        return "x:{} y:{}".format(self.x, self.y)
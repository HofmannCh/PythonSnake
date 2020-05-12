from models.Tile import Tile
from numpy import concatenate

class Grid:
    def __init__(self, sizeY, sizeX):
        self.sizeY = sizeY
        self.sizeX = sizeX
        self.tiles = [[Tile(y, x, self) for x in range(sizeX)] for y in range(sizeY)]

    def getTiles2D(self):
        return list(self.tiles)
    
    def getTiles1D(self):
        return list(concatenate(self.tiles))
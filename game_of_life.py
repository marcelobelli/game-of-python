class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = set()

    def add_cell(self, cell):
        self.cells.add(cell)


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

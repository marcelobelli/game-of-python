class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = set()

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.width == other.width and self.height == other.height and self.cells == other.cells

    def add_cell(self, cell):
        self.cells.add(cell)

    def next_iteration(self):
        self.cells = set()


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

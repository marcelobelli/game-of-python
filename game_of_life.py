from collections import defaultdict


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

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = set()

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.width == other.width and self.height == other.height and self.cells == other.cells

    def __repr__(self):
        return f"{self.cells}"

    def add_cell(self, cell):
        self.cells.add(cell)

    def next_iteration(self):
        will_die = set()
        can_live = defaultdict(int)
        for cell in self.cells:
            live_cells, empty_cells = self._get_adjacent_cells(cell)
            if len(live_cells) < 2:
                will_die.add(cell)

            for empty_cell in empty_cells:
                can_live[empty_cell] += 1

        for cell, count in can_live.items():
            if count == 3:
                self.cells.add(cell)

        self.cells -= will_die

    def _get_adjacent_cells(self, cell: Cell) -> tuple[set[Cell], set[Cell]]:
        """
        Get all adjacent cells from a given cell
        :param cell: A particular cell in the grid
        :return: set of adjacent cells from the given cell
        """
        offsets = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        live_cells = set()
        empty_cells = set()
        for offset in offsets:
            if Cell(cell.x + offset[0], cell.y + offset[1]) in self.cells:
                live_cells.add(Cell(cell.x + offset[0], cell.y + offset[1]))
            else:
                empty_cells.add(Cell(cell.x + offset[0], cell.y + offset[1]))

        return live_cells, empty_cells

from game_of_life import Cell, Grid


def test_grid_must_have_weight_and_width():
    grid = Grid(10, 10)
    assert grid.width == 10
    assert grid.height == 10


def test_cell_must_have_a_position():
    cell = Cell(1, 1)
    assert cell.x == 1
    assert cell.y == 1


def test_grid_cannot_have_duplicated_cells():
    grid = Grid(10, 10)
    cell_1 = Cell(1, 1)
    cell_2 = Cell(1, 1)
    grid.add_cell(cell_1)
    grid.add_cell(cell_2)
    assert len(grid.cells) == 1


def test_grid_can_have_multiple_cells():
    grid = Grid(10, 10)
    cell_1 = Cell(1, 1)
    cell_2 = Cell(2, 2)
    grid.add_cell(cell_1)
    grid.add_cell(cell_2)
    assert len(grid.cells) == 2

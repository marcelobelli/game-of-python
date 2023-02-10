from game_of_life import Cell, Grid


def test_grid_must_have_weight_and_width():
    grid = Grid(10, 10)
    assert grid.width == 10
    assert grid.height == 10


def test_cell_must_have_a_position():
    cell = Cell(1, 1)
    assert cell.x == 1
    assert cell.y == 1

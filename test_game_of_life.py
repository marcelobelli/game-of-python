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


def test_each_cell_with_one_or_no_neighbors_dies_as_if_by_solitude_first_example():
    """
    0 0 X       X X X
    X X X   ->  X X X
    X X 0       X X X
    """
    grid = Grid(3, 3)
    grid.add_cell(Cell(0, 0))
    grid.add_cell(Cell(0, 1))
    grid.add_cell(Cell(2, 2))
    expected_next_iteration = Grid(3, 3)

    assert grid != expected_next_iteration

    grid.next_iteration()

    assert grid == expected_next_iteration


def test_each_cell_with_one_or_no_neighbors_dies_as_if_by_solitude_second_example():
    """
    0 X 0       X X X
    X X X   ->  X X X
    0 X 0       X X X
    """
    grid = Grid(3, 3)
    grid.add_cell(Cell(0, 0))
    grid.add_cell(Cell(0, 2))
    grid.add_cell(Cell(2, 0))
    grid.add_cell(Cell(2, 2))
    expected_next_iteration = Grid(3, 3)

    assert grid != expected_next_iteration

    grid.next_iteration()

    assert grid == expected_next_iteration


def test_each_cell_with_two_neighbors_survives():
    """
    X X 0       X X X
    X 0 X   ->  X 0 X
    0 X X       X X X
    """
    grid = Grid(3, 3)
    grid.add_cell(Cell(0, 2))
    grid.add_cell(Cell(1, 1))
    grid.add_cell(Cell(2, 0))
    expected_next_iteration = Grid(3, 3)
    expected_next_iteration.add_cell(Cell(1, 1))

    assert grid != expected_next_iteration

    grid.next_iteration()

    assert grid == expected_next_iteration

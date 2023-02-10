from game_of_life import Grid


def test_grid_must_have_weight_and_width():
    grid = Grid(10, 10)
    assert grid.width == 10
    assert grid.height == 10

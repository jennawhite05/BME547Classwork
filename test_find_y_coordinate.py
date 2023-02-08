import pytest

# getting tuple input - don't need a test for this

# getting x input variable - don't need a test 

#parsing (x, y) values -- parse string into a list of tuples

@pytest.mark.parametrize("coords_input, x_input,  expected", [(((3, 2), (4, 6)), 0, -10),
                                                 (((2, 4), (4, 8)), 3, 6),
                                                 (((-1, 9), (1, 8))), 2, 8.5])
def test_find_y_value(coords_input, x_input, expected):
    from find_y_coordinate import find_y_value
    answer = find_y_value(coords_input, x_input)
    # Assert
    assert answer == expected

@pytest.mark.parametrize("coordinates, expected", [(((3, 2), (4, 6)), 4),
                                                 (((2, 4), (4, 8)), 2),
                                                 (((-1, 9), (1, 8))), -0.5])
#getting slope
def test_calculate_slope(coordinates, expected):
    from finding_y_coordinate import calculate_slope
    answer = calculate_slope(coordinates)
    # Assert
    assert answer == expected

#getting y-intercept
@pytest.mark.parametrize("coordinates, slope, expected", [((3, 2), 4, -10),
                                                 ((2, 4), 2, 0),
                                                 ((-1, 9), -0.5, 8.5)])
def test_find_intercept(coordinates, slope, expected):
    from finding_y_coordinate import find_intercept
    answer = find_intercept(coordinates, slope)
    # Assert
    assert answer == expected


#outputting y value - don't need a test for this 

#(3, 2)
#(4,6)

# (6-2)/(4-3) = 4/1 = 4




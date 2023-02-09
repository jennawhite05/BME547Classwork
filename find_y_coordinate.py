def coordinates_input():
    coordinates = input("Enter two points: ")
    realpoints = eval(coordinates)
    return realpoints


def x_input():
    x = input("Enter x value: ")
    realx = float(x)
    return realx


def find_y_value(coordinates, x):
    slope = calculate_slope(coordinates)
    y_intercept = find_intercept(coordinates[0], slope)
    y = slope*x + y_intercept
    return y


def calculate_slope(coordinates):
    first_x = coordinates[0][0]
    first_y = coordinates[0][1]
    second_x = coordinates[1][0]
    second_y = coordinates[1][1]
    slope = (second_y-first_y)/(second_x-first_x)
    print("The line has a slope of {}.". format(slope))
    return slope


def find_intercept(coordinates, slope):
    x = coordinates[0]
    y = coordinates[1]
    intercept = y - slope*x
    print("The line has a y-intercept of {}.". format(intercept))
    return intercept


def y_output(x, y):
    print("At an x-value of {} on the line, the y-value will be {}."
          .format(x, y))


if __name__ == "__main__":
    coordinates = coordinates_input()
    x = x_input()
    y = find_y_value(coordinates, x)
    y_output(x, y)

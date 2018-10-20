from math import pow, sqrt


def get_index(array2d, item):
    for list in array2d:
        if item in list:
            return array2d.index(list), list.index(item)
    return False


def get_abs_difference(x, y):
    return abs(x - y)


def get_abs_diff_squared(x, y):
    return pow(get_abs_difference(x, y), 2)


def get_manhattan(currentState):
    manhattan_distance = 0
    for i in range(0, 3):
        for j in range(0, 3):
            item = 3 * i + j
            index = get_index(currentState, item)
            x = get_abs_difference(index[0], i)
            y = get_abs_difference(index[1], j)
            manhattan_distance = manhattan_distance + x + y
    return manhattan_distance


def get_euclidean(currentState):
    euclidean_distance = 0
    for i in range(0, 3):
        for j in range(0, 3):
            item = 3 * j + i
            index = get_index(currentState, item)
            x = get_abs_diff_squared(index[0], i)
            y = get_abs_diff_squared(index[1], j)
            euclidean_distance = euclidean_distance + sqrt(x + y)
    return euclidean_distance

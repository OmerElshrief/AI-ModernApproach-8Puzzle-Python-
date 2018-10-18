# Transforms any 1d array to 2d
# @param: array1d (list)
# @returns: list of lists, each list n
def to_matrix(array1d, n):
    return [array1d[i:i + n] for i in range(0, len(array1d), n)]

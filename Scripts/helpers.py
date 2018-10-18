"""Transforms any 1d array to 2d
 @param: array1d (list)
 @returns: list of lists, each list n"""


def to_matrix(array1d, n):
    return [array1d[i:i + n] for i in range(0, len(array1d), n)]


class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()

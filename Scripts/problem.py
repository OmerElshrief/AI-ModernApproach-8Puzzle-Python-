class Problem:

    def __init__(self, initial, goal=None):
        self.initialState = initial
        # The Goal of our problem, We will use this variable to perform the GoalTest""
        self.goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    """Function: Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
    """The Possible actions are NORTH,SOUTH,EAST,WEST"""
    """NORTH = 1, SOUTH =2, EAST =3, WEST=4"""

    def getActions(self, state):
        i, j = self.getZeroPosition(state)
        if i == 0:
            if j == 0:  # The First block of the Board, The Zero position may only go to EAST and SOUTH
                return 2, 3
            if j == 1:  # The Second block of the Board, The Zero position may go to EAST , SOUTH and WEST
                return 2, 3, 4
            if j == 2:  # The Third block of the Board, The Zero position may go to SOUTH and WEST
                return 2, 4

        if i == 1:
            if j == 0:  # The Fourth block of the Board, The Zero position may go to NoORTH, EAST and SOUTH
                return 1, 2, 3
            if j == 1:  # The Fifth block of the Board, The Zero position may go to any position
                return 1, 2, 3, 4
            if j == 2:  # The Sixth block of the Board, The Zero position may  go to NORTH, WEST and SOUTH
                return 4, 2, 1

        if i == 2:
            if j == 0:  # The Seventh block of the Board, The Zero position may go to NoORTH, EAST
                return 1, 3
            if j == 1:  # The Eighth block of the Board, The Zero position may go to NORTH, EAST and WEST
                return 1, 3, 4
            if j == 2:  # The Ninth block of the Board, The Zero position may  go to NORTH, WEST
                return 1, 4

    """Function: Returns a new state when the given action is executed in the given State"""

    def getNewState(self, state, action):
        i, j = self.getZeroPosition(state)

        newState = deepcopy(state)  # We need a copy of the current State to do the action and generate a new state
        # It's sufficient to keep the current state unchanged because it's being used by the searching algo.

        if action == 1:  # Action of the Zero going NORTH
            # Swapping the Zero Region with the Upper Region by
            newState[i][j], newState[i - 1][j] = newState[i - 1][j], newState[i][j]
        elif action == 2:  # Action of going SOUTH
            # Swapping the Zero Region with the Lower Region by
            newState[i][j], newState[i + 1][j] = newState[i + 1][j], newState[i][j]
        elif action == 3:  # Action of going EAST
            # Swapping the Zero Region with the Right Region by
            newState[i][j], newState[i][j + 1] = newState[i][j + 1], newState[i][j]
        elif action == 4:  # Action of going WEST
            # Swapping the Zero Region with the Left Region by
            newState[i][j], newState[i][j - 1] = newState[i][j - 1], newState[i][j]

        return newState

    """Function to Perform the Goal Test"""

    def goalTest(self, state):
        if self.goalState == state:
            return True
        return False

    def getZeroPosition(self, state):

        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

        return 0, 0

    def getSolution(self, goalNode=Node(0, 0, 0, 0)):
        node = Node(0, 0, 0, 0)
        node = goalNode
        count = 0;
        print("Path cost = ", node.path_cost)
        print("\n")
        while goalNode:
            print(goalNode.state)
            goalNode = goalNode.parent
            count += 1
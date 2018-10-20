# this is to be exported and used to map the values returned by the get actions to add steps to each node
actions = {
    1: "Up",
    2: "Down",
    3: "Left",
    4: "Right"
}

rev_actions = {
    "Up": 1,
    "Down": 2,
    "Left": 3,
    "Right": 4

}

"""A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total cost (also known as g) to reach the node."""


class Node:
    def __init__(self, state, parent, action, depth, cost=None):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.action = action
        self.cost = cost
        if cost is None:
            self.cost = depth


class SearchTree:
    def __init__(self, state):
        self.root = Node(state, None, "Initial", 0)
        self.children = []
        self.nodes_expanded = 0
        self.goal = None
        self.max_depth = 0

    def get_root(self):
        return self.root

    def get_goal(self):
        return self.goal

    def get_child(self, state, parent, action, depth, cost=None):
        child = Node(state, parent, action, depth, cost)
        self.children.append(child)
        if child.depth > self.max_depth:
            self.max_depth = child.depth
        return child

    def set_nodes_expanded(self):
        self.nodes_expanded = self.nodes_expanded + 1

    def set_goal(self, node):
        self.goal = node


"""The abstract class for a formal problem. You should subclass
this and implement the methods actions and result, and possibly
__init__, goal_test, and cost. Then you will create instances
of your subclass and solve them with the various search functions. """


class Problem:

    def __init__(self, initial=None):
        self.initialState = initial
        # The Goal of our problem, We will use this variable to perform the GoalTest""
        self.goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    """Function: Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
    """The Possible actions are NORTH,SOUTH,EAST,WEST"""
    """NORTH = 1, SOUTH =2, WEST=3, EAST=4"""

    def getActions(self, state):
        i, j = self.getZeroPosition(state)
        if i == 0:
            if j == 0:  # The First block of the Board, The Zero position may only go to EAST and SOUTH
                return [2, 4]
            if j == 1:  # The Second block of the Board, The Zero position may go to EAST , SOUTH and WEST
                return [2, 3, 4]
            if j == 2:  # The Third block of the Board, The Zero position may go to SOUTH and WEST
                return [2, 3]

        if i == 1:
            if j == 0:  # The Fourth block of the Board, The Zero position may go to NoORTH, EAST and SOUTH
                return [1, 2, 4]
            if j == 1:  # The Fifth block of the Board, The Zero position may go to any position
                return [1, 2, 3, 4]
            if j == 2:  # The Sixth block of the Board, The Zero position may  go to NORTH, WEST and SOUTH
                return [1, 2, 3]

        if i == 2:
            if j == 0:  # The Seventh block of the Board, The Zero position may go to NoORTH, EAST
                return [1, 4]
            if j == 1:  # The Eighth block of the Board, The Zero position may go to NORTH, EAST and WEST
                return [1, 3, 4]
            if j == 2:  # The Ninth block of the Board, The Zero position may  go to NORTH, WEST
                return [1, 3]

    """Function: Returns a new state when the given action is executed in the given State"""

    def getNewState(self, state, action):
        i, j = self.getZeroPosition(state)

        newState = [oldState[:] for oldState in state]
        # We need a copy of the current State to do the action and generate a new state
        # It's sufficient to keep the current state unchanged because it's being used by the searching algo.

        if action == 1:  # Action of the Zero going NORTH
            # Swapping the Zero Region with the Upper Region by
            newState[i][j], newState[i - 1][j] = newState[i - 1][j], newState[i][j]
        elif action == 2:  # Action of going SOUTH
            # Swapping the Zero Region with the Lower Region by
            newState[i][j], newState[i + 1][j] = newState[i + 1][j], newState[i][j]
        elif action == 4:  # Action of going EAST
            # Swapping the Zero Region with the Right Region by
            newState[i][j], newState[i][j + 1] = newState[i][j + 1], newState[i][j]
        elif action == 3:  # Action of going WEST
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

    def getSolution(self, tree=SearchTree(-1), time=None, searchName="None Specified"):
        f = open("log.txt", "a")
        f.write("------------------------" + searchName + "------------------------\n")
        steps = []
        cost = 0
        goalNode = tree.get_goal()
        while goalNode:
            cost = cost+goalNode.cost
            print(goalNode.state)
            f.write(str(goalNode.state) + "\n")
            steps.append(goalNode.action)
            goalNode = goalNode.parent

        # resetting goal node as it was changed in while loop
        goalNode = tree.get_goal()
        print("Path cost = ", goalNode.depth)
        print("Path depth = ", goalNode.depth)
        print("Max depth = ", tree.max_depth)
        print("Nodes Expanded = ", tree.nodes_expanded)
        print("time Taken = ", time)
        # remove "initial"
        steps.pop()
        steps.reverse()
        print("Steps = " + str(steps) + "\n")

        f.write("Steps = " + str(steps) + "\n")
        f.write("Path cost = " + str(goalNode.cost) + "\n")
        f.write("Path depth = " + str(goalNode.depth) + "\n")
        f.write("Nodes Expanded = " + str(tree.nodes_expanded) + "\n")
        f.write("time Taken = " + str(time) + "\n")

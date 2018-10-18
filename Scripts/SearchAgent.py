from collections import *
from Scripts.problem import *
from Scripts.helpers import *
import sys


"""Abstracted Class for the Problem Solving Agent"""


class SearchAgent:

    # function to solve a given problem using BFS
    def __init__(self, state={}):
        self.state = state

    def breadth_first_search(self, problem):
        node = Node(problem.initialState, None, "initial", 0, 0)

        frontier = deque()
        frontier.append(node)
        explored = []
        while frontier:
            current = frontier.popleft()
            explored.append(current)

            # getting all possible actions as a list
            possibleActions = problem.getActions(current.state)

            if problem.goalTest(current.state):
                return problem.getSolution(current)

            for action in possibleActions:
                child = Node(problem.getNewState(current.state, action), current, actions.get(action), current.path_cost + 1,
                             current.nodes_expanded+len(frontier)+1)
                if not (any(prev.state == child.state for prev in explored) or any(prev.state == child.state for prev in
                                                                                   frontier)):
                    frontier.append(child)
        return False

    def depth_first_search(self, problem):
        node = Node(problem.initialState, None, "initial", 0, 0)

        frontier = [node]
        explored = []
        expanded = 0

        while frontier:
            current = frontier.pop()
            explored.append(current)

            # getting all possible actions as a list
            possibleActions = problem.getActions(current.state)
            # Number of expanded nodes at any given node is the number of possible moves
            expanded = expanded+len(possibleActions)
            for action in possibleActions:
                child = Node(problem.getNewState(current.state, action), current, actions.get(action),
                             current.path_cost + 1,
                             expanded)
                if problem.goalTest(current.state):
                    return problem.getSolution(child)
                if child not in explored and child not in frontier:
                    frontier.append(child)
        return False


        # if problem.goalTest(node.state):
        #     return problem.getSolution(node.state)
        # frontier = Stack()
        # explored = list()
        # visited = list()
        # frontier.add(node)
        # visited.append(node.state)
        # while frontier:
        #     node = frontier.remove()
        #     for action in problem.getActions(node.state):
        #         child = Node(problem.getNewState(node.state, action), node, action, node.path_cost + 1)
        #
        #         if problem.goalTest(child.state):
        #             return problem.getSolution(child)
        #         if child.state not in visited and child not in explored:
        #             frontier.add(child)
        #             visited.append(child.state)
        #
        #     explored.append(node)
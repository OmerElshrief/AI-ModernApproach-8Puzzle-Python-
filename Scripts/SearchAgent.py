import queue
from Scripts.problem import *
from Scripts.helpers import *
import sys


"""Abstracted Class for the Problem Solving Agent"""


class SearchAgent:

    # function to solve a given problem using BFS
    def __init__(self, state={}):
        self.state = state

    def breadth_first_search(self, problem):
        node = Node(problem.initialState, None, None, 0)

        if problem.goalTest(node.state):
            return problem.getSolution(node.state)
        frontier = queue.Queue()
        explored = list()
        visited = list()
        frontier.put(node)
        visited.append(node)
        while frontier:
            node = frontier.get()

            for action in problem.getActions(node.state):
                child = Node(problem.getNewState(node.state, action), node, action, node.path_cost + 1)
                if problem.goalTest(child.state):
                    return problem.getSolution(child)
                if child not in visited and child not in explored:
                    frontier.put(child)
                    visited.append(child)

            explored.append(node)

    def depth_first_search(self, problem):
        node = Node(problem.initialState, None, None, 1)

        if problem.goalTest(node.state):
            return problem.getSolution(node.state)
        frontier = Stack()
        explored = list()
        visited = list()
        frontier.add(node)
        visited.append(node.state)
        while frontier:
            node = frontier.remove()
            for action in problem.getActions(node.state):
                child = Node(problem.getNewState(node.state, action), node, action, node.path_cost + 1)

                if problem.goalTest(child.state):
                    return problem.getSolution(child)
                if child.state not in visited and child not in explored:
                    frontier.add(child)
                    visited.append(child.state)

            explored.append(node)
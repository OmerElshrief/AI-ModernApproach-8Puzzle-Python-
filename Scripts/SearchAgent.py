import queue
from collections import deque
from copy import copy, deepcopy
import tkinter
import sys


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


"""A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node."""


class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost


"""The abstract class for a formal problem. You should subclass
this and implement the methods actions and result, and possibly
__init__, goal_test, and path_cost. Then you will create instances
of your subclass and solve them with the various search functions. """




"""Abstracted Class for the Problem Solving Agent"""


class SearchAgent:

    # function to solve a given problem using BFS
    def __init__(self, state={}):
        self.state = state

    def breadth_first_search(self, problem):
        node = Node(problem.initialState, None, None, 0)

        if (problem.goalTest(node.state)):
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

        if (problem.goalTest(node.state)):
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

    def uniform_cost_search(self, problem):

        node = Node(problem.initialState, None, None, 0)

        if (problem.goalTest(node.state)):
            return problem.getSolution(node.state)
        frontier = queue.PriorityQueue()
        explored = list()
        visited = list()
        frontier.put(node)
        visited.append(node)
        while frontier:
            node = frontier.get()

            for action in problem.getActions(node.state):
                child = Node(problem.getNewState(node.state, action), node, action, node.path_cost + 1)
                print(child.state)
                if problem.goalTest(child.state):
                    return problem.getSolution(child)
                if child not in visited and child not in explored:
                    frontier.put(child)
                    visited.append(child)

        explored.append(node)


# Testing
initialCondition = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
problem = Problem(initialCondition)
agent = SearchAgent()
agent.breadth_first_search(problem)
print("DFS: \n")
agent.depth_first_search(problem)
print("UCS: \n")
agent.uniform_cost_search(problem)
top = tkinter.Tk()
top.mainloop()

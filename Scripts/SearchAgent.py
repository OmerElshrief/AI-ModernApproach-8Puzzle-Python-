import queue
from Scripts.problem import *
from Scripts.helpers import *
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


"""Initializer function to start"""


def main():
    # Our test case: 1,2,5,3,4,0,6,7,8
    puz_str = input("Welcome \n please input your puzzle comma seperated:")

    # Parse input into a list
    puzzle = puz_str.split(",")

    # loop to trim any input with spaces in list and type cast input
    for i in range(0, len(puzzle)):
        puzzle[i] = int(puzzle[i].strip())

    initialCondition = to_matrix(puzzle, 3)
    problem = Problem(initialCondition)
    agent = SearchAgent()

    while True:
        user_choice = input("Would you like:\n"
                            "1) BFS\n"
                            "2) DFS\n"
                            "3) A*\n"
                            "type 'exit' to escape\n")
        if user_choice == "1":
            print("BFS: \n")
            agent.breadth_first_search(problem)
        elif user_choice == "2":
            print("DFS: \n")
            agent.depth_first_search(problem)
        elif user_choice == "3":
            print("A*: \n")
            agent.a_star_search(problem)
        elif user_choice == "exit":
            break


main()

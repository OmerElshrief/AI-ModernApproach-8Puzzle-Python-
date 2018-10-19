from collections import *
from Scripts.problem import *
from Scripts.helpers import *
import heapq
import time

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
        start = time.time()

        while frontier:
            current = frontier.popleft()
            explored.append(current)

            # getting all possible actions as a list
            possibleActions = problem.getActions(current.state)

            print("current:")
            print(current.state)

            if problem.goalTest(current.state):
                now = time.time() - start
                return problem.getSolution(current, now)

            for action in possibleActions:
                child = Node(problem.getNewState(current.state, action), current, actions.get(action),
                             current.path_cost + 1,
                             current.nodes_expanded+len(frontier)+1)

                if not (any(prev.state == child.state for prev in explored) or any(prev.state == child.state for prev in
                                                                                   frontier)):
                    frontier.append(child)
        now = time.time() - start
        print("Failure! Time:")
        print(now)

    def depth_first_search(self, problem):
        node = Node(problem.initialState, None, "initial", 0, 0)
        frontier = [node]
        explored = []
        start = time.time()
        while frontier:
            current = frontier.pop()
            explored.append(current)

            # getting all possible actions as a list
            possibleActions = problem.getActions(current.state)
            possibleActions.reverse()

            print("current:")
            print(current.state)

            if problem.goalTest(current.state):
                now = time.time() - start
                return problem.getSolution(current, now)

            for action in possibleActions:
                child = Node(problem.getNewState(current.state, action), current, actions.get(action),
                             current.path_cost + 1,
                             current.nodes_expanded + len(frontier) + 1)
                if not (any(prev.state == child.state for prev in explored) or any(prev.state == child.state for prev in
                                                                                   frontier)):
                    frontier.append(child)
            now = time.time() - start
            print("Failure! Time:")
            print(now)

    def a_star_search(self, problem):
        node = Node(problem.initialState, None, "initial", 0, 0)
        frontier = []
        heapq.heappush(frontier, node)
        explored = []
        start = time.time()

        while frontier:
            current = heapq.heappop(frontier)
            
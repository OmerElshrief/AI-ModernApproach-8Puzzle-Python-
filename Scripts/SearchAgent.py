from collections import *
from Scripts.problem import *
from Scripts.helpers import *
from Scripts.heuristic import *
import heapq as H
import time

"""Abstracted Class for the Problem Solving Agent"""


class SearchAgent:

    # function to solve a given problem using BFS
    def __init__(self, state=None):
        if state is None:
            state = {}
        self.state = state

    def breadth_first_search(self, problem):
        tree = SearchTree(problem.initialState)
        frontier = deque()
        frontier.append(tree.get_root())
        explored = []
        start = time.time()

        while frontier:
            current = frontier.popleft()
            explored.append(current)

            # getting all possible actions as a list
            possibleActions = problem.getActions(current.state)

            print("current:")
            print(current.state)
            print('Explored: ', tree.nodes_expanded)

            if problem.goalTest(current.state):
                now = time.time() - start
                tree.set_goal(current)
                return problem.getSolution(tree, now, "BFS")
            tree.set_nodes_expanded()

            for action in possibleActions:
                child = tree.get_child(problem.getNewState(current.state, action), current, actions.get(action),
                                       current.depth + 1)

                if not (any(prev.state == child.state for prev in explored) or any(prev.state == child.state for prev in
                                                                                   frontier)):
                    frontier.append(child)
        now = time.time() - start
        print("Failure! Time:")
        print(now)

    def depth_first_search(self, problem):
        tree = SearchTree(problem.initialState)
        frontier = [tree.get_root()]
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
            print('Explored: ', tree.nodes_expanded)

            if problem.goalTest(current.state):
                now = time.time() - start
                tree.set_goal(current)
                return problem.getSolution(tree, now, "DFS")
            tree.set_nodes_expanded()

            for action in possibleActions:
                child = tree.get_child(problem.getNewState(current.state, action), current, actions.get(action),
                                       current.depth + 1)
                if not (any(prev.state == child.state for prev in explored) or any(prev.state == child.state for prev in
                                                                                   frontier)):
                    frontier.append(child)
        now = time.time() - start
        print("Failure! Time:")
        print(now)

    def a_star_search(self, problem):
        self.a_star_search_manhattan(problem)

    def decrease_key(self, frontier, neighbor):
        heaped = [(cost, currentAction, state, node) for cost, currentAction,state, node in frontier]

        for item in heaped:
            index = heaped.index(item)
            print("HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEee", neighbor.state, neighbor.cost, item[2], item[0])
            if neighbor.state == item[2] and neighbor.cost < item[0]:
                print("INNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
                heaped[index] = node_to_tuple_with_time(neighbor)
        return heaped

    def print_f(self, frontier):
        heaped = [(cost, currentAction, state, node) for cost,currentAction, state, node in frontier]
        H.heapify(heaped)
        print("heap:")
        while heaped:
            print(H.heappop(heaped))

    def a_star_search_manhattan(self, problem):
        tree = SearchTree(problem.initialState)

        # to use priority in the heaps I am going to use a tuple with 3 data inputs cost, state and NODE
        tree.root.cost = get_manhattan(tree.root.state)
        frontier = [node_to_tuple_with_time(tree.get_root())]
        H.heapify(frontier)
        explored = []
        start = time.time()

        while frontier:
            cost, currentAction, state, current = H.heappop(frontier)
            explored.append(current)

            # getting all possible actions as a list
            possibleActions = problem.getActions(current.state)

            print("current:")
            print(current.state)
            print('Explored: ', tree.nodes_expanded)

            if problem.goalTest(current.state):
                now = time.time() - start
                tree.set_goal(current)
                return problem.getSolution(tree, now, "A*-Manhattan")
            tree.set_nodes_expanded()

            for action in possibleActions:
                childState = problem.getNewState(current.state, action)
                child = tree.get_child(childState, current, actions.get(action),
                                       current.depth + 1, current.cost - get_manhattan(current.state)+get_manhattan(childState) + 1)
                # print("child: ", childState, get_manhattan(childState))

                if any(state == child.state for cost, currentAction, state, current in frontier):
                    frontier = self.decrease_key(frontier, child)

                elif not any(prev.state == child.state for prev in explored):
                    H.heappush(frontier, node_to_tuple_with_time(child))
                    # print(H.heappop(frontier))
            self.print_f(frontier)
            H.heapify(frontier)

        now = time.time() - start
        print("Failure! Time:")
        print(now)

    def a_star_search_euclidean(self, problem):
        tree = SearchTree(problem.initialState)

        # to use priority in the heaps I am going to use a tuple with 3 data inputs cost, state and NODE
        frontier = [tree.get_root()]
        H.heapify(frontier)
        explored = []
        start = time.time()

        while frontier:
            cost, state, current = H.heappop(frontier)
            explored.append(current)

            # getting all possible actions as a list
            possibleActions = problem.getActions(current.state)

            if problem.goalTest(current.state):
                now = time.time() - start
                tree.set_goal(current)
                return problem.getSolution(tree, now, "A*-Euclidean")
            tree.set_nodes_expanded()

            for action in possibleActions:
                child = tree.get_child(problem.getNewState(current.state, action), current, actions.get(action),
                                       current.depth + 1, 1)

                if not (any(prev.state == child.state for prev in explored) or any(
                        prev.state == child.state for prev in
                        frontier)):
                    frontier.append(child)

        now = time.time() - start
        print("Failure! Time:")
        print(now)

from Scripts.SearchAgent import *

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
from Scripts.SearchAgent import *

"""Initializer function to start"""


def main():
    # Our test case: 1,2,5,3,4,0,6,7,8
    # 3,1,2,0,4,5,6,7,8 up
    # 3,1,2,6,4,5,0,7,8 up up
    # 3,0,2,6,1,5,7,4,8 down down left up up
    # 1,4,2,3,0,5,6,7,8
    # 1,4,2,0,3,5,6,7,8
    # 6,1,8,4,0,2,7,3,5
    # 8,6,4,2,1,3,5,7,0
    #0,6,4,7,3,8,1,5,2
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

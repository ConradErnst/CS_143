from Problem import *

# [[4,1,3,2]
#  [2,3,4,1]
#  [1,4,2,3]
#  [3,2,1,4]]

# -------------
# | 4 1 | 3 2 |
# | 2 3 | 4 1 |
# -------------
# | 1 4 | 2 3 |
# | 3 2 | 1 4 |
# -------------

class Sudoku(Problem):

    def __init__(self, initial):
        self.state = initial
        Problem.__init__(self, initial)

    def h(self, state):
        cost = 1

        # Need to come up with some cost evaluation
    
        return cost



    def display(self):
        map = {}
        count = 0
        for r in range(len(self.state)):
            for c in range(len(self.state[r])):
                map[count] = self.state[r][c]
                count += 1
        
        print("-------------")
        print(f"| {map[0]} {map[1]} | {map[2]} {map[3]} |")
        print(f"| {map[4]} {map[5]} | {map[6]} {map[7]} |")
        print("-------------")
        print(f"| {map[8]} {map[9]} | {map[10]} {map[11]} |")
        print(f"| {map[12]} {map[13]} | {map[14]} {map[15]} |")
        print("-------------")


    def is_solved(self, state):
        valid = True
        for r in range(len(state)):
            for c in range(len(state[r])):
                ...
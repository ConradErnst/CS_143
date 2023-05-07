from queue import PriorityQueue
from Node import *
import time
import pdb

class AStarSearch():

    def __init__(self, problem):
        self.problem = problem
        self.nodesSearched = 0
        self.timeSpent = 0

    def search(self):
        return self.astar(self.problem.initial)
    
    def astar(self, startState):
        startTime = time.time()

        root = Node(startState, path_cost = 0)
        root.fCost = self.problem.h(root.state)

        frontier = PriorityQueue()
        frontier.put((0, root))
        frontierStates = {}
        frontierStates[root.state] = root

        explored = set()

        while not frontier.empty():
            element = frontier.get()
            node = element[1]

            self.nodesSearched += 1
            if self.problem.is_solved(node.state):
                self.timeSpent = time.time() - startTime
                return node
            
            explored.add(node.state)

            for action in self.problem.actions(node.state):
                nextState = self.problem.result

                if nextState not in explored:
                    child = Node(state=nextState, parent=node,
                                 path_cost=self.problem.path_cost(node.path_cost, node.state, action, nextState),
                                 action=action)
                    
                    child.fCost = child.path_cost + self.problem.h(child.state)
                    frontier.put((child.fCost, child))
                    frontierStates[child.state] = child

        self.timeSpent = time.time() - startState
        return None
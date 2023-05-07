from Sudoku import *
from AStarSearch import *

unsolved = Sudoku([[1,4," ",3],[2,3,4," "],[" ",1,3,2],[3," ",1,4]])

print("Starting board:")
unsolved.display()

myAstarSearch = AStarSearch(unsolved)
result = myAstarSearch.search()

print("Completed board:")
result.display()
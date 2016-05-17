'''
Algorithms from Khan Academy
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-17
First Created: 2016-May-17
Python 2.7
Chris
'''

edgeList = [ [0, 2], [1, 3], [2, 3], [2, 4], [3, 5], [4, 5] ]

adjMatrix = [[0 for x in range(6)] for x in range(6)]
adjMatrix[0][2] = 1
adjMatrix[1][3] = 1
adjMatrix[2][3] = 1
adjMatrix[2][4] = 1
adjMatrix[3][5] = 1
adjMatrix[4][5] = 1

adjList = [[2], [3], [3, 4], [5], [5], []]

print edgeList

for x in range(6):
    print adjMatrix[x]

print adjList

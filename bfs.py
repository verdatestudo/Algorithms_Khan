'''
Algorithms from Khan Academy
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-17
First Created: 2016-May-17
Python 2.7
Chris
'''

def bfs(graph, start_pos):
    '''
    BFS
    '''
    node_bfs = [[float('inf'), None] for x in graph] # for each node, set default distance and parent
    queue = [start_pos] # enq starting node
    node_bfs[start_pos][0] = 0 # starting node distance = 0

    while queue:
        current_node = queue.pop(0) # FIFO queue rather than LIFO stack

        for nebor in graph[current_node]:
            if node_bfs[nebor][0] == float('inf'): # if not visited
                node_bfs[nebor][0] = node_bfs[current_node][0] + 1 # distance = parent distance + 1
                node_bfs[nebor][1] = current_node # set it's parent
                queue.append(nebor) #enq

    return node_bfs


graph = [[1], [0, 4, 5], [3, 4, 5], [2, 6], [1, 2], [1, 2, 6], [3, 5], []]
result = bfs(graph, 3)

for node in result:
    print node

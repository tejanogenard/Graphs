from util import Queue 
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    
    # Ancestors will be an array of the path of vertices 
    # we're going to trace our graph and make a path until we reach a vertex with no ancestors 
    # if multiple vertices have no more ancestors we can return the last value of the longest path 
    # check if a vertex as two earliest ancestors we want to compare and return the lowest num ancestor 
    # if vertex has no ancestors return -1. 

    # dictionary to store our vertices 
    # we'll use ancestors as the key and the children as the value 
    vertices = {}
    


    for parent, child in ancestors: 
        # if child not in vertices:
        vertices[child] = set() 

        #checking if parent is not in vertices 
        #we'll set the parents key to value of child 
        # if parent not in vertices:
            # vertices[parent] = child


    for parent, child in ancestors: 
        vertices[child] = vertices[child].add(parent)
        # lets add our starting node to the queue
    

    print(vertices)
    q = Queue()
    q.enqueue([starting_node])

    #While the queue is not empty... 
    # while q.size() > 0:
    #     #Dequeue the first Path
    #     path = q.dequeue()
        
        # if no parents return -1 
        
        # otherwise pass parents into the 
        # queue if there are multiple parents add the lowest of them 
        # to the queue. 

        # once we get to the end and we have no more parents we can print that value 
    

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]



earliest_ancestor(test_ancestors, 1)

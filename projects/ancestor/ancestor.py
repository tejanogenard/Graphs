from util import Queue 
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    
# Use the ancestor information to build a graph
        # Don't need a full graph, just information about what its parents are
# Put it in a dictionary, the second value is the key and the first value is added to the list of neighbors
# {node ID: [list of parents]}
# For each node in the ancestors list, Initialize the key in the dictionary, and Add the parents into the value list
# This creates a dictionary of all the nodes that have parents
# If the node doesn't have a parent it isn't in the dictionary

# Breadth first traversal saving completed paths to a list

# Start at the starting node, if it has parents add the parents' paths to the queue
        # If it doesn't have parents that is the end of the path, add the completed path to the output list
# Look at the last item in the path to see if that item has parents
        # if it does, add path to each parent to the queue
        # If it doesn't, add that path to the output list
# Create an empty queue
# Enque a path to the starting node
# Create a set to store visited paths
# Create a list to store paths to compare lengths
# While the queue is not empty
    # Dequeue the first path
    # Grab the last node of the path
    # If the vertex has not been visited:
         # add it to visited
         # if the vertex is in the dictionary (i.e. if it has parents)
                # Add a path to its parents to the queue
                # Copy the path, Append the parent vertex to it, Add the next path to the end of the queue
 # If v doesn't have any parents, add the completed path to the list of paths
# If we are here, we have calculated all the completed paths from the starting node
    # Find the longest path
    # If there are two longest paths, return the lower value end node
        # Sort the list by length of lists
            # If there is a tie sort again by the last value, ascending
    # Our oldest ancestor is the last item of the first list
 # If there is no paths (only the starting node), return -1
    # If the resulting path is equal to the starting node, return -1

    q = Queue()
    cache = {}
    current = starting_node

    q.enqueue(starting_node)

    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        if child not in cache: 
            cache[child] = parent
            print(cache)


    
    

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]



earliest_ancestor(test_ancestors, 1)




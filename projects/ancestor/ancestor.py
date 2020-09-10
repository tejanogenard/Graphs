

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)



def earliest_ancestor(ancestors, starting_node):

    vertices = {} 

# set our children as our keys and the parents as the value of each key 

    for i in ancestors: 
        if i[1] not in vertices: 
            vertices[i[1]] = set() 

        vertices[i[1]].add(i[0])



    def get_ancestors(vertex_id):
    
        if vertex_id in vertices.keys():
            return vertices[vertex_id]
        else: 
            return [None]

            # queue our starting node 
    q = Queue()
    # Initialize queue with starting the starting nod
    q.enqueue([starting_node])
    # create our visited set for our verticies   
    visited = set() 
    # create our path that we will be returning 
    family_tree = []

            # While the queue is not empty 
    while q.size() > 0:

        
        family_path = q.dequeue()

        ancestor = family_path[-1]

        # if the ancestor is not in the visited set 
        if ancestor not in visited: 
            
            # added the ancestor to the visited set 
            visited.add(ancestor)

            # add all the ancestors to the queue 
            for child in get_ancestors(ancestor):
                if child is not None:
                    family_copy = family_path.copy()
                    family_copy.append(ancestor)
                    q.enqueue(family_copy)
                elif ancestor == starting_node:
                    return -1 

            family_tree.append(family_path)

    path = []

    for i in family_tree:
        if len(i) > len(path):
            path = i 

    return path[-1]


    
    





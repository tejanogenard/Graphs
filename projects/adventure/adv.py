from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"


# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# def traverse_map(): 
   # initalize a reversed set to traverse in a opposite direction 
   # create a visited set
   # initalize our path 
   # get all exits for the current room
   # travel in available direction
   # check to see if a room has been visited 
   # if not, add room to visited set 
   # add the direction of the next room to traversal path 
   # if we reach a dead end, then move in the opposite direction

   

visited = {}



def traverse_map():
    backwards = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    path = []
    # get all possible directions for a room
    for direction in player.current_room.get_exits():
        #travel in a direction
        player.travel(direction)
        #if the room has been visited before 
        if player.current_room.id in visited:
            # travel in the opposite direction
            player.travel(backwards[direction])
        else:
            # else add the room to the visited 
            visited[player.current_room.id] = player.current_room.id 
            # add the direction of the room to the path 
            path.append(direction)
            #call traverse_map for the next room
            path += traverse_map() 
            # travel in the opposite direction
            player.travel(backwards[direction])
            # add the reverse travel to  the path 
            path.append(backwards[direction])
    return path
    
traversal_path = traverse_map()




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

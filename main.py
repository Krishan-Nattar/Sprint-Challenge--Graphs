from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

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
# world.print_rooms()

player = Player(world.starting_room)

traversal_path = []
visited = {}
room_id_stack = Stack()
current_room_id = player.current_room.id

directed_path = []
append_count = 684
count = 0

def bfs(starting, ending):
    '''
    Take a starting room id and an ending room id. Find the shortest path between the two.
    Return a list of cardinal movements to move the player to that spot.
    '''
    queue = Queue()
    bfs_visited = set()
    queue.enqueue([(starting)])
    current_path = []
    movement_path = []
    while queue.size() > 0:
        current_path = queue.dequeue()
        current_node = current_path[-1]
        if current_node == ending:
            break
        if current_node not in bfs_visited:
            bfs_visited.add(current_node)
            edges = room_graph[current_node][1]
            for edge in edges:
                queue.enqueue(current_path + [room_graph[current_node][1][edge]])

    path_length = len(current_path)
    path_length -= 1
    for i in range(path_length):
        node = current_path[i]
        edges = room_graph[node][1]
        for edge in edges:
            if room_graph[node][1][edge] == current_path[i+1]:
                movement_path.append(edge)
    return movement_path

def directed_movement(direction):
    '''
    This moves player in the given direction.
    Visited gets initialized if the player has not been to the room before.
    Cardinal directions for both rooms are set to the room ids
    Traversal path is appended
    '''
    global traversal_path

    curr_dir_id = player.current_room.id
    curr_dir_exits = player.current_room.get_exits()
    room_id_stack.push(curr_dir_id)
    if curr_dir_id not in visited:
        create_room(curr_dir_id, curr_dir_exits)

    player.travel(direction)
    new_dir_id = player.current_room.id
    new_dir_exits = player.current_room.get_exits()

    if new_dir_id not in visited:
        create_room(new_dir_id, new_dir_exits)

    visited[curr_dir_id][direction] = new_dir_id
    reverse = reverse_letters(direction)

    visited[new_dir_id][reverse] = curr_dir_id

    traversal_path.append(direction)

def reverse_letters(letter):
    '''
    Here we take a cardinal direction and return the opposite direction
    '''
    if letter == 'n':
        return 's'
    if letter == 's':
        return 'n'
    if letter == 'e':
        return 'w'
    if letter == 'w':
        return 'e'

    # Can return from a dictionary

def create_room(id, exits):
    '''
    Create a new room and add all exits with '?' attached to to them
    '''
    visited[id] = {}
    for exit in exits:
        visited[id][exit] = '?'

def check_exits_and_move():
    '''
    Check all exits in current room.
    If room has an exit(s) that has not been explored yet, randomly move in one of those directions.
    If room the room contained an unexplored room, we return True, otherwise return False
    '''
    # Initialize current room variables
    first_room = player.current_room
    first_room_id = first_room.id
    first_room_exits = first_room.get_exits()

    # This will hold all cardinal directions 
    unexplored_edges = []

    # Check if any exit contains '?'
    for exit in visited[first_room_id]:
        if visited[first_room_id][exit] == '?':
            unexplored_edges.append(exit)

    # This will run if there are any possible unexplored directions to move towards
    if len(unexplored_edges) > 0:

        # Pick a random direction out of all unexplored directions
        direction = random.choice(unexplored_edges)
        
        # Move player
        directed_movement(direction)

        # Return True to indicate that a new room was successfully found and moved to
        return True

    # Return False to indicate that no viable unexplored exits could be found
    return False

def do_exits_exist(room_id):
    '''
    Checks a given room id to see if there are unexplored rooms.
    If there are unexplored rooms, return True, otherwise return false
    '''
    cardinal_list = visited[room_id]
    for direction in cardinal_list:
        if visited[room_id][direction] == '?':
            return True
    return False

def begin_traversal():
    '''
    Traverse the map until every room has been visited at least once.
    Every movement will append the cardinal direction to the traversal_map list
    '''

    while len(visited) < len(room_graph):

        first_room = player.current_room
        first_room_id = first_room.id
        first_room_exits = first_room.get_exits()
        room_id_stack.push(first_room_id)
        '''
        If the current room has not been visited yet, we create the room
        '''
        if first_room_id not in visited:
            create_room(first_room_id, first_room_exits)

        '''
        Check to see if the current room has available exits to move through
        '''
        movement = check_exits_and_move()

        '''
        If no available movements, we backtrack to find previous node with a '?'
        '''
        if movement is False:

            while room_id_stack.size() > 0:
                node_2 = room_id_stack.pop()

                rooms_exist = do_exits_exist(node_2)
                if rooms_exist == True:
                    initialized_path = bfs(player.current_room.id,node_2)
                    for item in initialized_path:
                        directed_movement(item)
                    break

print("Begin Traversal")

begin_traversal()

# TRAVERSAL TEST
print(traversal_path)
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

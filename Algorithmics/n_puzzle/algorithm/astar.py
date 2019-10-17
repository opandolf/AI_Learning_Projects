import queue as Q
from algorithm.Node import Node

def actions(state, size):
    actions = []
    idx = state.split(",").index('0')
    if idx > size - 1:
        actions.append("UP")
    if idx < size*(size - 1):
        actions.append("DOWN")
    if idx % size != 0:
        actions.append("LEFT")
    if idx % size != (size - 1):
        actions.append("RIGHT")
    return actions 

def result(state,action, size):
    result = state.split(",")
    idx = result.index('0')
    tile_idx = -1
    if action == "UP": 
        tile_idx = idx - size
    elif action == "DOWN":
        tile_idx = idx + size
    elif action == "LEFT":
        tile_idx = idx - 1
    elif action == "RIGHT":
        tile_idx = idx + 1
    result[idx], result[tile_idx] = result[tile_idx], result[idx]
    return ','.join(result)

def solved(state, goal):
    state_array = state.split(",")
    goal_array = goal.split(",")
    for i in range(len(goal_array)):
        if (goal_array[i] != 'x' and goal_array[i] != state_array[i]):
            return False
    return True

def astar(start, goal, cost_function, heuristic_function, size, greedy):
#The open and closed sets
    opened = Q.PriorityQueue()
    explored = set()
    #Current point is the starting point
    current = start
    #Add the starting point to the open set
    opened.put(current)
    explored.add(current.state)
    total_opened = 1
    max_opened = 1
    #While the open set is not empty
    while opened:
        #Find the item in the open set with the lowest G + H score
        current = opened.get()
        # print("explored:" + str(len(explored)) + "  H: " + str(current.H) + " G: " + str(current.G) + " F: " + str(current.G + current.H))
        #If it is the item we want, retrace the path and return it
        if solved(current.state, goal):
            path = []
            while current.parent:
                path.append(current.state)
                current = current.parent
            path.append(current.state)
            return path[::-1], total_opened, max_opened
        #Loop through the node's children/siblings
        if greedy:
            opened = Q.PriorityQueue()
        for action in actions(current.state,size):
            state = result(current.state,action, size)
            #If it is already in the closed set, skip it
            if state in explored:
                continue
            explored.add(state)
            node = Node(state)
            #calculate the G and H score for the node
            node.G = current.G + cost_function()
            node.H = heuristic_function(state, goal, size)
            #Set the parent to our current item
            node.parent = current
            #Add it to the set
            opened.put(node)
            total_opened += 1
            if opened.qsize() > max_opened:
                max_opened = opened.qsize()
    #Throw an exception if there is no path
    print("No Solution")
    exit()

from heuristic.Point import Point

def manhattan_distance(state, goal, size):
    res = 0
    state_array = state.split(",")
    goal_array = goal.split(",")
    for i in range(len(goal_array)):
        if (str(state_array[i]) in goal_array):
            state_point =  Point(i, size)
            goal_point = Point(goal_array.index(str(state_array[i])), size)
            res += state_point.distance(goal_point)
    return res
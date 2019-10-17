from heuristic.manhattant_distance import manhattan_distance
from heuristic.Point import Point

def point_in_segment(a,b,c):
    if(a >= min(b,c) and a <= max(b,c)):
        return True
    else:
        return False

def linear_conflict(state, goal, size):
    state_array = state.split(",")
    goal_array = goal.split(",")
    res = 0
    for a in range(len(goal_array)):
        if (str(state_array[a]) in goal_array):
            a_state = Point(a, size)
            a_goal = Point(goal_array.index(str(state_array[a])), size)
            if(a_state.x == a_goal.x or a_state.y == a_goal.y):
                for b in range(a + 1, len(goal_array)):
                    if (str(state_array[b]) in goal_array):
                        b_state = Point(b, size)
                        b_goal = Point(goal_array.index(str(state_array[b])), size)
                        if(a_state == a_goal and b_state == b_goal):
                            continue
                        if(a_state.x == a_goal.x == b_state.x == b_goal.x and (point_in_segment(a_state.x, b_state.x, b_goal.x) or point_in_segment(b_state.x, a_state.x, a_goal.x))):
                            res += 2
                            continue
                        if(a_state.y == a_goal.y == b_state.y == b_goal.y and (point_in_segment(a_state.y, b_state.y, b_goal.y) or point_in_segment(b_state.y, a_state.y, a_goal.y))):
                            res += 2
                            continue
    return res


def linear_conflict_manhattan(state, goal, size):
    return manhattan_distance(state, goal, size) + linear_conflict(state, goal, size)
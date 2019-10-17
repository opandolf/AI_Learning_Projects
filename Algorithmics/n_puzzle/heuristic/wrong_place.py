def wrong_place(state, goal, size):
    result = 0
    state_array = state.split(",")
    goal_array = goal.split(",")
    for x in range(size*size):
        if (state_array[x] != goal_array[x]):
            result += 1
    return result
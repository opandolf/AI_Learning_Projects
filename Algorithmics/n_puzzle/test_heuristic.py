from heuristic_set.linear_conflict_set import linear_conflict

state = "4,2,5,1,0,6,3,8,7"
goal = "1,2,3,4,5,6,7,8,0"
size = 3
print(linear_conflict(state, goal, size))

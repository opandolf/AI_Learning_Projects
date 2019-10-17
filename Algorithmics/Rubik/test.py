from Cube import Cube
import numpy as np

def generate_scramble(choices, n):
    scramble = ""
    for _ in range(n):
        scramble += np.random.choice(choices) + " "
    return scramble

def mask_diff(a,b):
    mask = []
    for i in range(len(a)):
        if a[i] == b[i]:
            mask += [0]
        else:
            mask += [1]
    return mask
    
init = [x for x in range(12)]

# c = Cube(init, None)
# c.print_edges()
# print(c.edges_ori)
# c.formula("F R U B L D")

# c.formula("U D L' F' U' R' D' U2 B2 D'")
# print(c.edges_ori)
# c.print_edges()

ok = 0
total_count = 0
num_sim = 1#000
choices = ["U", "U2", "U'", "D", "D2", "D'", "F", "F2", "F'", "B", "B2", "B'", "R", "R2", "R'", "L", "L2", "L'"]
# for i in range(num_sim):
    # scramble = generate_scramble(choices, 10)
scramble = "L' R R' F' L R2 L' R' F2 L"
    # print (scramble)
c = Cube()
c.formula(scramble)
    # c.solve_white_cross()
    # c.solve_white_corners()
    # c.solve_second_layer()
    # c.solve_yellow_cross()
    # c.solve_yellow_corners()
    # c.solve_corners_last_layer()
    # c.solve_edges_last_layer()
solution, count = c.solve()
    # total_count += count
    # if c.check_valid():
        # ok += 1
    # else:
        # print(scramble)
# print("ok : ",  ok)
# print(total_count / num_sim)
print (solution)

# c = Cube()
# scramble = "D' L2 U' U2 B2 D' L U' F B'"
# c.formula(scramble)
# print("scramble : ", scramble)
# print("white_cross : ",c.solve_white_cross())
# c.print_corner()
# print("white_corners : ",c.solve_white_corners())
# c.print_corner()
# print("second_layer : ",c.solve_second_layer())
# print("yellow_cross : ",c.solve_yellow_cross())
# print("yellow_corners : ",c.solve_yellow_corners())
# print("corner PLL :", c.solve_corners_last_layer())
# print("edge PLL :", c.solve_edges_last_layer())
# print(c.check_valid())

# c = Cube()
# c.formula("F U R U' R' F'")
# print(c.edges_ori)
# c.formula("F U R U' R' F'")
# print(c.edges_ori)
# c.formula("F U R U' R' F'")
# print(c.edges_ori)
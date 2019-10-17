edge_position_dict = {
    "U": [3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
    "U2": [2, 3, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11],
    "U'": [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11],

    "D": [0, 1, 2, 3, 5, 6, 7, 4, 8, 9, 10, 11],
    "D2": [0, 1, 2, 3, 6, 7, 4, 5, 8, 9, 10, 11],
    "D'": [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],

    "F": [0, 9, 2, 3, 4, 8, 6, 7, 1, 5, 10, 11],
    "F2": [0, 5, 2, 3, 4, 1, 6, 7, 9, 8, 10, 11],
    "F'": [0, 8, 2, 3, 4, 9, 6, 7, 5, 1, 10, 11],

    "B": [0, 1, 2, 11, 4, 5, 6, 10, 8, 9, 3, 7],
    "B2": [0, 1, 2, 7, 4, 5, 6, 3, 8, 9, 11, 10],
    "B'": [0, 1, 2, 10, 4, 5, 6, 11, 8, 9, 7, 3],

    "R": [8, 1, 2, 3, 11, 5, 6, 7, 4, 9, 10, 0],
    "R2": [4, 1, 2, 3, 0, 5, 6, 7, 11, 9, 10, 8],
    "R'": [11, 1, 2, 3, 8, 5, 6, 7, 0, 9, 10, 4],

    "L": [0, 1, 10, 3, 4, 5, 9, 7, 8, 2, 6, 11],
    "L2": [0, 1, 6, 3, 4, 5, 2, 7, 8, 10, 9, 11],
    "L'": [0, 1, 9, 3, 4, 5, 10, 7, 8, 6, 2, 11]
}

edge_orientation_dict = {
    "U": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "U2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "U'": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    "D": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "D2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "D'": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    "F": [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    "F2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "F'": [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],

    "B": [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    "B2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "B'": [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],

    "R": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "R2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "R'": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    "L": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "L2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "L'": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}

corner_position_dict = {
    "U": [3, 0, 1, 2, 4, 5, 6, 7],
    "U2": [2, 3, 0, 1, 4, 5, 6, 7],
    "U'": [1, 2, 3, 0, 4, 5, 6, 7],

    "D": [0, 1, 2, 3, 5, 6, 7, 4],
    "D2": [0, 1, 2, 3, 6, 7, 4, 5],
    "D'": [0, 1, 2, 3, 7, 4, 5, 6],

    "F": [1, 5, 2, 3, 0, 4, 6, 7],
    "F2": [5, 4, 2, 3, 1, 0, 6, 7],
    "F'": [4, 0, 2, 3, 5, 1, 6, 7],

    "B": [0, 1, 3, 7, 4, 5, 2, 6],
    "B2": [0, 1, 7, 6, 4, 5, 3, 2],
    "B'": [0, 1, 6, 2, 4, 5, 7, 3],

    "R": [4, 1, 2, 0, 7, 5, 6, 3],
    "R2": [7, 1, 2, 4, 3, 5, 6, 0],
    "R'": [3, 1, 2, 7, 0, 5, 6, 4],

    "L": [0, 2, 6, 3, 4, 1, 5, 7],
    "L2": [0, 6, 5, 3, 4, 2, 1, 7],
    "L'": [0, 5, 1, 3, 4, 6, 2, 7]
}

corner_orientation_dict = {
    "U": [0, 0, 0, 0, 0, 0, 0, 0],
    "U2": [0, 0, 0, 0, 0, 0, 0, 0],
    "U'": [0, 0, 0, 0, 0, 0, 0, 0],

    "D": [0, 0, 0, 0, 0, 0, 0, 0],
    "D2": [0, 0, 0, 0, 0, 0, 0, 0],
    "D'": [0, 0, 0, 0, 0, 0, 0, 0],

    "F": [1, 2, 0, 0, 2, 1, 0, 0],
    "F2": [0, 0, 0, 0, 0, 0, 0, 0],
    "F'": [1, 2, 0, 0, 2, 1, 0, 0],

    "B": [0, 0, 1, 2, 0, 0, 2, 1],
    "B2": [0, 0, 0, 0, 0, 0, 0, 0],
    "B'": [0, 0, 1, 2, 0, 0, 2, 1],

    "R": [2, 0, 0, 1, 1, 0, 0, 2],
    "R2": [0, 0, 0, 0, 0, 0, 0, 0],
    "R'": [2, 0, 0, 1, 1, 0, 0, 2],

    "L": [0, 1, 2, 0, 0, 2, 1, 0],
    "L2": [0, 0, 0, 0, 0, 0, 0, 0],
    "L'": [0, 1, 2, 0, 0, 2, 1, 0]  
}

edge_value_dict = {
    0 : ['y', 'r'],
    1:['y','b'],
    2:['y','o'],
    3:['y','g'],
    4 : ['w', 'r'],
    5:['w','b'],
    6:['w','o'],
    7:['w','g'],
    8:['b','r'],
    9:['b','o'],
    10:['g','o'],
    11:['g','r']
}

corner_value_dict = {
    0:['y','r','b'],
    1:['y','b','o'],
    2:['y','o','g'],
    3:['y','g','r'],
    4:['w','b','r'],
    5:['w','o','b'],
    6:['w','g','o'],
    7:['w','r','g']
}

class Cube:
    def __init__(self):
        self.edges = [x for x in range(12)]
        self.edges_ori = [0] * 12
        self.corners = [x for x in range(8)]
        self.corners_ori = [0] * 8

    def rotation(self, notation):
        
        edge_pos = edge_position_dict[notation]
        edge_ori = edge_orientation_dict[notation]
        corner_pos = corner_position_dict[notation]
        corner_ori = corner_orientation_dict[notation]

        new_edges = [0] * 12
        new_edges_ori = [0] * 12
        for i in range(12):
            new_edges[i] = self.edges[edge_pos[i]]
            new_edges_ori[i] = (self.edges_ori[edge_pos[i]] + edge_ori[i]) % 2

        new_corner = [0] * 8
        new_corner_ori = [0] * 8
        for i in range(8):
            new_corner[i] = self.corners[corner_pos[i]]
            new_corner_ori[i] = (self.corners_ori[corner_pos[i]] + corner_ori[i]) % 3

        self.edges = new_edges
        self.edges_ori = new_edges_ori
        self.corners = new_corner
        self.corners_ori = new_corner_ori

    def formula(self, formula_str):
        formula_list = filter(None,formula_str.split(" "))
        for notation in formula_list:
            self.rotation(notation)

    def print_edges(self):
        for i in range(12):
            x = self.edges[i]
            if self.edges_ori[i] == 0:
                c1 = edge_value_dict[x][0]
                c2 = edge_value_dict[x][1]
                o = "o"
            else:
                c2 = edge_value_dict[x][0]
                c1 = edge_value_dict[x][1]
                o = "x"
            print("%2d %2d : %s | %s | %s" % (i, x, c1, c2, o))
        print()

    def print_corner(self):
        for i in range(8):
            x = self.corners[i]
            c = corner_value_dict[x]
            o = self.corners_ori[i]
            c = c[(3-o) % 3:] + c[:(3-o) % 3]
            print("%2d %2d : %s | %s | %s , %d" % (i, x, c[0], c[1], c[2], o))


    def solve_white_red(self):
        idx = self.edges.index(4)
        # print("idx : ", idx)

        oriented = True if self.edges_ori[idx] == 0 else False

        if idx == 0:
            if oriented:
                return "R2"
            else:
                return "U F R'"
        elif idx == 1:
            if oriented:
                return "U' R2"
            else:
                return "F R'"
        elif idx == 2:
            if oriented:
                return "U2 R2"
            else:
                return "U' F R'"
        elif idx == 3:
            if oriented:
                return "U R2"
            else:
                return "B' R"
        
        elif idx == 4:
            if oriented:
                return ""
            else:
                return "R F D"
        elif idx == 5:
            if oriented:
                return "D"
            else:
                return "F' R'"
        elif idx == 6:
            if oriented:
                return "D2"
            else:
                return "D F' R'"
        elif idx == 7:
            if oriented:
                return "D'"
            else:
                return "B R"
        
        elif idx == 8:
            if oriented:
                return "R'"
            else:
                return "F D"
        elif idx == 9:
            if oriented:
                return "L D2"
            else:
                return "F' D"
        elif idx == 10:
            if oriented:
                return "L' D2"
            else:
                return "B D'"
        elif idx == 11:
            if oriented:
                return "R"
            else:
                return "B' D'"

    def solve_white_blue(self):
        idx = self.edges.index(5)
        # print("idx : ", idx)

        oriented = True if self.edges_ori[idx] == 0 else False

        if idx == 0:
            if oriented:
                return "U F2"
            else:
                return "R' F R"
        elif idx == 1:
            if oriented:
                return "F2"
            else:
                return "U L F'"
        elif idx == 2:
            if oriented:
                return "U' F2"
            else:
                return "L F'"
        elif idx == 3:
            if oriented:
                return "U2 F2"
            else:
                return "U' L F'"
        
        elif idx == 5:
            if oriented:
                return ""
            else:
                return "F D' L D"
        elif idx == 6:
            if oriented:
                return "L' D' L D"
            else:
                return "L' F'"
        elif idx == 7:
            if oriented:
                return "B D2 B' D2"
            else:
                return "B' D' L' D"
        
        elif idx == 8:
            if oriented:
                return "D R' D'"
            else:
                return "F"
        elif idx == 9:
            if oriented:
                return "D' L D"
            else:
                return "F'"
        elif idx == 10:
            if oriented:
                return "D' L' D"
            else:
                return "D2 B D2"
        elif idx == 11:
            if oriented:
                return "D R D'"
            else:
                return "D2 B' D2"

    def solve_white_orange(self):
        idx = self.edges.index(6)
        # print("idx : ", idx)
        oriented = True if self.edges_ori[idx] == 0 else False

        if idx == 0:
            if oriented:
                return "U2 L2"
            else:
                return "U' B L'"
        elif idx == 1:
            if oriented:
                return "U L2"
            else:
                return "F' L F"
        elif idx == 2:
            if oriented:
                return "L2"
            else:
                return "U' F' L F"
        elif idx == 3:
            if oriented:
                return "U' L2"
            else:
                return "B L'"
        
        elif idx == 6:
            if oriented:
                return ""
            else:
                return "L D' B D"
        elif idx == 7:
            if oriented:
                return "B D' B' D"
            else:
                return "B' L'"
        
        elif idx == 8:
            if oriented:
                return "D2 R' D2"
            else:
                return "D F D'"
        elif idx == 9:
            if oriented:
                return "L"
            else:
                return "D F' D'"
        elif idx == 10:
            if oriented:
                return "L'"
            else:
                return "D' B D"
        elif idx == 11:
            if oriented:
                return "D2 R D2"
            else:
                return "D' B' D"

    def solve_white_green(self):
        idx = self.edges.index(7)
        # print("idx : ", idx)
        oriented = True if self.edges_ori[idx] == 0 else False

        if idx == 0:
            if oriented:
                return "U' B2"
            else:
                return "R B' R'"
        elif idx == 1:
            if oriented:
                return "U2 B2"
            else:
                return "U' R B' R'"
        elif idx == 2:
            if oriented:
                return "U B2"
            else:
                return "L' B L"
        elif idx == 3:
            if oriented:
                return "B2"
            else:
                return "U R B' R'"
        
        elif idx == 7:
            if oriented:
                return ""
            else:
                return "B' D L' D'"
        
        elif idx == 8:
            if oriented:
                return "D' R' D"
            else:
                return "D2 F D2"
        elif idx == 9:
            if oriented:
                return "D L D'"
            else:
                return "D2 F' D2"
        elif idx == 10:
            if oriented:
                return "D L' D'"
            else:
                return "B"
        elif idx == 11:
            if oriented:
                return "D' R D"
            else:
                return "B'"

    def solve_white_cross(self):
        wr = self.solve_white_red()
        # print("wr : " + wr)
        self.formula(wr)
        # self.print_edges()

        wb = self.solve_white_blue()
        # print("wb : " + wb)
        self.formula(wb)
        # self.print_edges()
        
        wo = self.solve_white_orange()
        # print("wo : " + wo)
        self.formula(wo)
        # self.print_edges()

        wg = self.solve_white_green()
        # print("wg : " + wg)
        self.formula(wg)
        # self.print_edges()

        # self.print_corner()
        return wr + " " + wb + " " + wo + " " + wg + " "
    
    def solve_white_blue_red(self):
        idx = self.corners.index(4)
        # print(idx)
        orientation = self.corners_ori[idx]

        f0 = "R U2 R' U' R U R'"
        f1 = "R U R'"
        f2 = "F' U' F"

        if orientation == 0:
            f = f0
        elif orientation == 1:
            f = f1
        else:
            f = f2

        if idx == 0:
            return f
        elif idx == 1:
            return "U' " + f
        elif idx == 2:
            return "U2 " + f
        elif idx == 3:
            return "U " + f


        elif idx == 4:
            if orientation == 0:
                return ""
            elif orientation == 1:
                return "F' U' F U " + f2
            else:
                return "R U R' U' " + f1
        elif idx == 5:
            if orientation == 0:
                return "L' U' L " + f1
            elif orientation == 1:
                return "L' U' L " + f2
            else:
                return "F U F' U2 " + f1
        elif idx == 6:
            if orientation == 0:
                return "B' U2 B " + f1
            elif orientation == 1:
                return "B' U2 B " + f2
            else:
                return "L U2 L' " + f1
        else:
            if orientation == 0:
                return "B U B' " + f2
            elif orientation == 1:
                return "R' U2 R U' " + f2
            else:
                return "B U B' " + f1

    def solve_white_orange_blue(self):
        idx = self.corners.index(5)
        # print(idx)
        orientation = self.corners_ori[idx]

        f0 = "F U2 F' U' F U F'"
        f1 = "F U F'"
        f2 = "L' U' L"

        if orientation == 0:
            f = f0
        elif orientation == 1:
            f = f1
        else:
            f = f2

        if idx == 0:
            return "U " + f
        elif idx == 1:
            return f
        elif idx == 2:
            return "U' " + f
        elif idx == 3:
            return "U2 " + f

        elif idx == 5:
            if orientation == 0:
                return ""
            elif orientation == 1:
                return "L' U' L U " + f2
            else:
                return "F U F' U' " + f1
        elif idx == 6:
            if orientation == 0:
                return "B' U' B " + f1
            elif orientation == 1:
                return "B' U' B " + f2
            else:
                return "L U L' U2 " + f1
        else:
            if orientation == 0:
                return "R' U2 R " + f1
            elif orientation == 1:
                return "R' U2 R " + f2
            else:
                return "B U2 B' " + f1

    def solve_white_green_orange(self):
        idx = self.corners.index(6)
        # print(idx)
        orientation = self.corners_ori[idx]

        f0 = "L U2 L' U' L U L'"
        f1 = "L U L'"
        f2 = "B' U' B"

        if orientation == 0:
            f = f0
        elif orientation == 1:
            f = f1
        else:
            f = f2

        if idx == 0:
            return "U2 " + f
        elif idx == 1:
            return "U " + f
        elif idx == 2:
            return f
        elif idx == 3:
            return "U' " + f

        elif idx == 6:
            if orientation == 0:
                return ""
            elif orientation == 1:
                return "B' U' B U " + f2
            else:
                return "L U L' U' " + f1
        else:
            if orientation == 0:
                return "R' U' R " + f1
            elif orientation == 1:
                return "R' U' R " + f2
            else:
                return "B U B' U2 " + f1

    def solve_white_red_green(self):
        idx = self.corners.index(7)
        # print(idx)
        orientation = self.corners_ori[idx]

        f0 = "B U2 B' U' B U B'"
        f1 = "B U B'"
        f2 = "R' U' R"

        if orientation == 0:
            f = f0
        elif orientation == 1:
            f = f1
        else:
            f = f2

        if idx == 0:
            return "U' " + f
        elif idx == 1:
            return "U2 " + f
        elif idx == 2:
            return "U " + f
        elif idx == 3:
            return  f

        else:
            if orientation == 0:
                return ""
            elif orientation == 1:
                return "R' U' R U " + f2
            else:
                return "B U B' U' " + f1

    def solve_white_corners(self):
        wbr = self.solve_white_blue_red()
        # print("wbr : ",wbr)
        self.formula(wbr)
        wob = self.solve_white_orange_blue()
        # print("wob : ", wob)
        self.formula(wob)
        wgo = self.solve_white_green_orange()
        # print("wgo : ", wgo)
        self.formula(wgo)
        wrg = self.solve_white_red_green()
        self.formula(wrg)
        return wbr + " " + wob + " " + wgo + " " + wrg + " "

    def solve_blue_red(self):
        idx = self.edges.index(8)
        # print("idx : ", idx)
        oriented = True if self.edges_ori[idx] == 0 else False

        rb = "U R U' R' U' F' U F"
        lb = "U' L' U L U F U' F'"

        ro = "U F U' F' U' L' U L"
        lo = "U' B' U B U L U' L'"        

        rg = "U L U' L' U' B' U B"
        lg = "U' R' U R U B U' B'"

        rr = "U B U' B' U' R' U R"
        lr = "U' F' U F U R U' R'"


        if idx == 0:
            if oriented:
                return lr
            else:
                return "U " + rb
        elif idx == 1:
            if oriented:
                return "U' " + lr
            else:
                return rb
        elif idx == 2:
            if oriented:
                return "U2 " + lr 
            else:
                return "U' " + rb
        elif idx == 3:
            if oriented:
                return "U " + lr
            else:
                return "U2 " + rb
        
        elif idx == 8:
            if oriented:
                return ""
            else:
                return rb + " U2 " + rb

        elif idx == 9:
            if oriented:
                return ro + " U " + rb
            else:
                return ro + " " + lr
        elif idx == 10:
            if oriented:
                return rg + " U' " + lr
            else:
                return rg + " " + rb
        else:
            if oriented:
                return rr + " U' " + rb
            else:
                return rr + " U2 " + lr

    def solve_blue_orange(self):
        idx = self.edges.index(9)
        # print("idx : ", idx)
        oriented = True if self.edges_ori[idx] == 0 else False

        rb = "U R U' R' U' F' U F"
        lb = "U' L' U L U F U' F'"

        ro = "U F U' F' U' L' U L"
        lo = "U' B' U B U L U' L'"        

        rg = "U L U' L' U' B' U B"
        lg = "U' R' U R U B U' B'"

        rr = "U B U' B' U' R' U R"
        lr = "U' F' U F U R U' R'"


        if idx == 0:
            if oriented:
                return "U2 " + ro
            else:
                return "U " + lb
        elif idx == 1:
            if oriented:
                return "U " + ro
            else:
                return lb
        elif idx == 2:
            if oriented:
                return ro
            else:
                return "U' " + lb
        elif idx == 3:
            if oriented:
                return "U' " + ro
            else:
                return "U2 " + lb
        
        elif idx == 9:
            if oriented:
                return ""
            else:
                return ro + " U2 " + ro
        elif idx == 10:
            if oriented:
                return rg + " U " + ro
            else:
                return lo + " U2 " + ro
        else:
            if oriented:
                return lg + " U " + ro
            else:
                return rr + " " + ro

    def solve_green_orange(self):
        idx = self.edges.index(10)
        # print("idx : ", idx)
        oriented = True if self.edges_ori[idx] == 0 else False

        rb = "U R U' R' U' F' U F"
        lb = "U' L' U L U F U' F'"

        ro = "U F U' F' U' L' U L"
        lo = "U' B' U B U L U' L'"        

        rg = "U L U' L' U' B' U B"
        lg = "U' R' U R U B U' B'"

        rr = "U B U' B' U' R' U R"
        lr = "U' F' U F U R U' R'"


        if idx == 0:
            if oriented:
                return "U2 " + lo
            else:
                return "U' " + rg
        elif idx == 1:
            if oriented:
                return "U " + lo
            else:
                return "U2 " + rg
        elif idx == 2:
            if oriented:
                return lo
            else:
                return "U " + rg
        elif idx == 3:
            if oriented:
                return "U' " + lo
            else:
                return rg
            

        elif idx == 10:
            if oriented:
                return ""
            else:
                return rg + " U2 " + rg
        else:
            if oriented:
                return rr + " U " + rg
            else:
                return lg + " U2 " + rg

    def solve_green_red(self):
        idx = self.edges.index(11)
        # print("idx : ", idx)
        oriented = True if self.edges_ori[idx] == 0 else False

        rb = "U R U' R' U' F' U F"
        lb = "U' L' U L U F U' F'"

        ro = "U F U' F' U' L' U L"
        lo = "U' B' U B U L U' L'"        

        rg = "U L U' L' U' B' U B"
        lg = "U' R' U R U B U' B'"

        rr = "U B U' B' U' R' U R"
        lr = "U' F' U F U R U' R'"


        if idx == 0:
            if oriented:
                return rr
            else:
                return "U' " + lg
        elif idx == 1:
            if oriented:
                return "U' " + rr
            else:
                return "U2 " + lg
        elif idx == 2:
            if oriented:
                return "U2 " + rr
            else:
                return "U " + lg
        elif idx == 3:
            if oriented:
                return "U " + rr
            else:
                return lg
            

        elif idx == 11:
            if oriented:
                return ""
            else:
                return rr + " U2 " + rr

    def solve_second_layer(self):
        br = self.solve_blue_red()
        # print("br : " + br)
        self.formula(br)
        bo = self.solve_blue_orange()
        # print("bo : " + bo)
        self.formula(bo)
        go = self.solve_green_orange()
        # print("go : " + go)
        self.formula(go)
        gr = self.solve_green_red()
        # print("gr : " + gr)
        self.formula(gr)
        return br + " " + bo + " " + go + " " + gr + " "

    def solve_yellow_cross(self):
        ret = ""
        while sum(self.edges_ori[:4]) != 0:
            if sum(self.edges_ori[2:4]) == 0:
                ret += "F U R U' R' F' "
                self.formula("F U R U' R' F' ")
            elif (self.edges_ori[0] == 0 and self.edges_ori[2] == 0) or sum(self.edges_ori[:4]) == 4:
                ret += "F R U R' U' F'"
                self.formula("F R U R' U' F' ")
            else:
                ret += "U "
                self.formula("U")
        return ret


# https://ruwix.com/the-rubiks-cube/advanced-cfop-fridrich/orient-the-last-layer-oll/
    def solve_yellow_corners(self):

        ret = ""
        while sum(self.corners_ori[:4]) != 0:
            sliced = self.corners_ori[:4]
            if sliced == [1,1,2,2]:
                ret += "L U' R' U L' U R U R' U R"
                self.formula("L U' R' U L' U R U R' U R")
            elif sliced == [1,2,1,2]:
                ret += "R U R' U R U' R' U R U2 R'"
                self.formula("R U R' U R U' R' U R U2 R'")
            elif sliced == [0,1,1,1]:
                ret += "L' U R U' L U R'"
                self.formula("L' U R U' L U R'")
            elif sliced == [0,2,2,2]:
                ret += "R' U2 R U R' U R"
                self.formula("R' U2 R U R' U R")
            elif sliced == [2,0,0,1]:
                ret += "R' F' L F R F' L' F"
                self.formula("R' F' L F R F' L' F")
            elif sliced == [2,1,0,0]:
                ret += "R2 D R' U2 R D' R' U2 R'"
                self.formula("R2 D R' U2 R D' R' U2 R'")
            elif sliced == [0,2,0,1]:
                ret += "R' F' L' F R F' L F"
                self.formula("R' F' L' F R F' L F")
            else:
                ret += "U "
                self.formula("U")
        return ret + " "
        
# https://cubingcheatsheet.com/algs3x_2lpll.html
    def solve_corners_last_layer(self):
        
        ret = ""
        positionned = [0 if self.corners[i] == i else 1 for i in range(4)]
        if positionned == [0,0,0,0]:
            return ret
        while positionned.count(0) != 2:
            ret += "U "
            self.formula("U")
            positionned = [0 if self.corners[i] == i else 1 for i in range(4)]
            if positionned == [0,0,0,0]:
                return ret
        if positionned == [0,1,0,1] or positionned == [1,0,1,0]:
            ret += "F R U' R' U' R U R' F' R U R' U' R' F R F'"
            self.formula("F R U' R' U' R U R' F' R U R' U' R' F R F'")
        else:
            if positionned == [1,1,0,0]:
                ret += "U' "
                self.formula("U'")
            elif positionned == [0,1,1,0]:
                ret += "U2 "
                self.formula("U2")
            elif positionned == [0,0,1,1]:
                ret += "U "
                self.formula("U")
            ret += "R U R' U' R' F R2 U' R' U' R U R' F'"
            self.formula("R U R' U' R' F R2 U' R' U' R U R' F'")

        positionned = [0 if self.corners[i] == i else 1 for i in range(4)]
        while positionned != [0,0,0,0]:
            ret += "U "
            self.formula("U")
            positionned = [0 if self.corners[i] == i else 1 for i in range(4)]

        return ret + " "

# https://cubingcheatsheet.com/algs3x_2lpll.html
    def solve_edges_last_layer(self):
        plla = "R2 U' R' U' R U R U R U' R"
        pllb = "R' U R' U' R' U' R' U R U R2"
        pllz = "R' U' R2 U R U R' U' R U R U' R U' R' U2"
        pllh = "L R U2 L' R' F' B' U2 F B"

        sliced = self.edges[:4]
        if sliced == [0,1,2,3]:
            return ""
        elif sliced == [2,3,0,1]:
            self.formula(pllh)
            return pllh
        elif sliced == [1,0,3,2]:
            self.formula(pllz)
            return pllz
        elif sliced == [3,2,1,0]:
            self.formula("U " + pllz + " U'")
            return "U " + pllz + " U'"
        
        positionned = [0 if self.edges[i] == i else 1 for i in range(4)]
        idx = positionned.index(0)
        if self.edges[(idx - 1) % 4] == (idx + 2) % 4:
            pll = plla
        else:
            pll = pllb
        if idx == 0:
            self.formula("U " + pll + " U'")
            return "U " + pll + " U'"
        elif idx == 1:
            self.formula(pll)
            return pll
        elif idx == 2:
            self.formula("U' " + pll + " U")
            return "U' " + pll + " U"
        else:
            self.formula("U2 " + pll + " U2")
            return "U2 " + pll + " U2"
        
    def solve(self):

        solution = ""
        solution += self.solve_white_cross()
        solution += self.solve_white_corners()
        solution += self.solve_second_layer()
        solution += self.solve_yellow_cross()
        solution += self.solve_yellow_corners()
        solution += self.solve_corners_last_layer()
        solution += self.solve_edges_last_layer()

        count = len(solution.split(" "))

        return solution, count
        
        
    def check_valid(self):

        if self.edges != [x for x in range(12)]:
            return False
        if self.edges_ori != [0] * 12:
            return False
        if self.corners != [x for x in range(8)]:
            return False
        if self.corners_ori != [0] * 8:
            return False
        return True
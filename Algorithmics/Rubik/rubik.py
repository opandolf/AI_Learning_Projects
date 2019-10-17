import argparse

import time
from Cube import Cube
import numpy as np

class ParsingError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def generate_scramble(choices, n):
    scramble = ""
    for _ in range(n):
        scramble += np.random.choice(choices) + " "
    return scramble

def detail_solution(c, scramble):
		solution = ""
		print ("White cross: ", c.solve_white_cross())
		print ("White corners: ", c.solve_white_corners())
		print ("Second layer: ", c.solve_second_layer())
		print ("Yellow cross: ", c.solve_yellow_cross())
		print ("Yellow corners: ", c.solve_yellow_corners())
		print ("Corners of last_layer: ", c.solve_corners_last_layer())
		print ("Edges of last layer: ", c.solve_edges_last_layer())
		c.formula(scramble)
		# solution, count = c.solve()
		# print (solution)

if __name__ == '__main__':
	choices = ["U", "U2", "U'", "D", "D2", "D'", "F", "F2", "F'", "B", "B2", "B'", "R", "R2", "R'", "L", "L2", "L'"]
	solution = ''
	count = 0
	arg_parser = argparse.ArgumentParser()
	group = arg_parser.add_mutually_exclusive_group()

	arg_parser.add_argument('-t', '--timer', action='store_true', help="print total execution time")
	arg_parser.add_argument('-g', '--generator', action='store_true', help="use integred generator")
	arg_parser.add_argument('-d', '--detail', action='store_true', help="detail solution for humain comprehension")

	arg_parser.add_argument("files", metavar="file", nargs="*")
	args = arg_parser.parse_args()

	
	if args.generator:
		size = input("Enter the size of scramble [1; 1000]\n")
		if not (size.isnumeric() and (int(size)) > 0 and (int(size)) <= 1000):
			print ("Invalid size, default = 15")
			size = 15
		scramble = generate_scramble(choices, int(size))
		print ("Generated scramble is : ", scramble)
		c = Cube()
		c.formula(scramble)
	else:
		scramble = args.files[0]

		print (scramble)
		toto = scramble.split(' ')
		for a in toto:
			if a not in choices:
				print ("Invalid scramble: ", a)
				exit(1)
		c = Cube()
		c.formula(scramble)
	if args.detail:
		detail_solution(c, scramble)
	if args.timer:
		start = time.time()
		solution, count = c.solve()
		end = time.time()
		print("exe time : {}".format(end - start))
	else:
		solution, count = c.solve()
	# print (solution)
	
	old = ""
	new = solution
	while old != new:
		old = new
		new = new.replace("  ", " ")

		new = new.replace("U U' ", "")
		new = new.replace("U' U ", "")
		new = new.replace("U U ", "U2 ")
		new = new.replace("U' U' ", "U2 ")
		new = new.replace("U2 U2 ", "")

		new = new.replace("D D' ", "")
		new = new.replace("D' D ", "")
		new = new.replace("D D ", "D2 ")
		new = new.replace("D' D' ", "D2 ")
		new = new.replace("D2 D2 ", "")

		new = new.replace("R R' ", "")
		new = new.replace("R' R ", "")
		new = new.replace("R R ", "R2 ")
		new = new.replace("R' R' ", "R2 ")
		new = new.replace("R2 R2 ", "")

		new = new.replace("L L' ", "")
		new = new.replace("L' L ", "")
		new = new.replace("L L ", "L2 ")
		new = new.replace("L' L' ", "L2 ")
		new = new.replace("L2 L2 ", "")

		new = new.replace("F F' ", "")
		new = new.replace("F' F ", "")
		new = new.replace("F F ", "F2 ")
		new = new.replace("F' F' ", "F2 ")
		new = new.replace("F2 F2 ", "")

		new = new.replace("B B' ", "")
		new = new.replace("B' B ", "")
		new = new.replace("B B ", "B2 ")
		new = new.replace("B' B' ", "B2 ")
		new = new.replace("B2 B2 ", "")

	print ("Solution: ", new)
from Game import Game
from Minimax import Minimax
from tkinter import *
from tkinter.messagebox import *
import time
import numpy as np
import argparse

class Board:
	def __init__(self, boardSize = 19, Largeur = 1000, Hauteur = 1000, canvasSize = (50, 50)):
		self.undostack = []
		self.boardSize = boardSize
		self.Largeur = Largeur
		self.Hauteur = Hauteur
		self.canvasSize = canvasSize
		self.vs_IA = True
		self.turn = 0
		self.time = 0

		self.game = Game(4, 0.5, "42", self.boardSize)
		self.minimax = Minimax(self.game, 10)
		self.node = self.game.init()
		self.id_table = np.zeros((self.game.size, self.game.size), dtype=int)
		self.create_board()
		self.create_widget()
		self.suggestion = [0,0,0,0]

	def create_board(self):
		# Création de la fenêtre principale (main window)
		self.Mafenetre = Tk()
		self.Mafenetre.title('Gomoku')
		# Image de fond
		try:
			self.photo = PhotoImage(file="board.gif")
		except:
			print ("don't remove the .gif ash-hole")
			exit (0)
		# Création d'un widget Canvas (zone graphique)
		self.Canevas = Canvas(self.Mafenetre, width = self.Largeur, height = self.Hauteur)
		self.item = self.Canevas.create_image(0,0,anchor=NW, image=self.photo)
		self.Canevas.pack(side=LEFT, padx =5, pady =5)

		c0, c1 = self.canvasSize
		for i in range(self.boardSize):
			self.Canevas.create_line(c0, c0 + c1*i, c0 + (self.boardSize-1)*c1, c0 + c1*i, fill='black')
			self.Canevas.create_line(c0 + c1*i, c0, c0 + c1*i, c0+(self.boardSize-1)*c1, fill='black')

	def New_game_IA_black(self):
		self.EffacerTout()
		self.node = self.game.init()
		self.vs_IA = True
		self.turn = 0
		self.tn.set(str(self.turn))
		child = self.minimax.iterative_deepening(self.node)
		for j in range(self.game.size):
			for i in range(self.game.size):
				if self.node.board[(j,i)] != child.board[(j,i)]:
					if child.board[(j,i)] != 0:
						self.id_table[(j,i)] = self.create_piece((j,i), child.board[(j,i)])
					else:
						self.Canevas.delete(self.id_table[(j,i)])
		self.node = child

	def New_game_IA_white(self):
		self.EffacerTout()
		self.node = self.game.init()
		self.vs_IA = True
		self.turn = 0
		self.tn.set(str(self.turn))

	def New_game_humain(self):
		self.EffacerTout()
		self.node = self.game.init()
		self.vs_IA = False
		self.turn = 0
		self.tn.set(str(self.turn))

	def New_game_hard(self):
		self.EffacerTout()
		self.game = Game(10, 20, "42", self.boardSize)
		self.minimax = Minimax(self.game, 10)
		self.node = self.game.init()
		self.vs_IA = True
		self.turn = 0
		self.tn.set(str(self.turn))
		child = self.minimax.iterative_deepening(self.node)
		for j in range(self.game.size):
			for i in range(self.game.size):
				if self.node.board[(j,i)] != child.board[(j,i)]:
					if child.board[(j,i)] != 0:
						self.id_table[(j,i)] = self.create_piece((j,i), child.board[(j,i)])
					else:
						self.Canevas.delete(self.id_table[(j,i)])
		self.node = child

	def New_game_normal(self):
		self.EffacerTout()
		self.game = Game(4, 0.5, "42", self.boardSize)
		self.minimax = Minimax(self.game, 10)
		self.node = self.game.init()
		self.vs_IA = True
		self.turn = 0
		self.tn.set(str(self.turn))

	def New_game_easy(self):
		self.EffacerTout()
		self.game = Game(1, 0.1, "42", self.boardSize)
		self.minimax = Minimax(self.game, 3)
		self.node = self.game.init()
		self.vs_IA = True
		self.turn = 0
		self.tn.set(str(self.turn))

	def New_game_Standard(self):
		self.EffacerTout()
		self.game = Game(4, 0.5, "standard", self.boardSize)
		self.minimax = Minimax(self.game, 10)
		self.node = self.game.init()
		self.vs_IA = True
		self.turn = 0
		self.tn.set(str(self.turn))

	def New_game_Pro(self):
		self.EffacerTout()
		self.game = Game(4, 0.5, "pro", self.boardSize)
		self.minimax = Minimax(self.game, 10)
		self.node = self.game.init()
		self.vs_IA = True
		self.turn = 0
		self.tn.set(str(self.turn))

	def New_game_Longpro(self):
		self.EffacerTout()
		self.game = Game(4, 0.5, "longpro", self.boardSize)
		self.minimax = Minimax(self.game, 10)
		self.node = self.game.init()
		self.vs_IA = True
		self.turn = 0
		self.tn.set(str(self.turn))

	def create_widget(self):
		Label(self.Mafenetre, text="Time exe:").pack(side = TOP, padx = 0, pady = 10)
		self.sv = StringVar()
		label_score = Label(self.Mafenetre, textvariable=self.sv)
		self.sv.set(str(self.time))
		label_score.pack(side = TOP, padx = 1, pady = 0)

		Label(self.Mafenetre, text="Black Captured:").pack(side = TOP, padx = 0, pady = 10)
		self.cb = StringVar()
		capture_black = Label(self.Mafenetre, textvariable=self.cb)
		self.cb.set(str(self.node.white_capture * 2))
		capture_black.pack(side = TOP, padx = 1, pady = 0)

		Label(self.Mafenetre, text="White Captured:").pack(side = TOP, padx = 0, pady = 10)
		self.cw = StringVar()
		capture_white = Label(self.Mafenetre, textvariable=self.cw)
		self.cw.set(str(self.node.black_capture * 2))
		capture_white.pack(side = TOP, padx = 1, pady = 0)

		Label(self.Mafenetre, text="Turn Number:").pack(side = TOP, padx = 0, pady = 10)
		self.tn = StringVar()
		turn_number = Label(self.Mafenetre, textvariable=self.tn)
		self.tn.set(str(self.node.black_capture * 2))
		turn_number.pack(side = TOP, padx = 1, pady = 0)

		# Création d'un widget nouvelle vs l'IA
		BoutonGo = Button(self.Mafenetre, text ='IA begin', command = self.New_game_IA_black)
		BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		# Création d'un widget nouvelle vs l'IA
		BoutonGo = Button(self.Mafenetre, text ='Humain begin', command = self.New_game_IA_white)
		BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		# Création d'un widget nouvelle partie a deux humain
		BoutonGo = Button(self.Mafenetre, text ='Two Humains game', command = self.New_game_humain)
		BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		Label(self.Mafenetre, text="Bonus:").pack(side = TOP, padx = 10, pady = 50)

		BoutonGo = Button(self.Mafenetre, text ='Easy', command = self.New_game_easy)
		BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		BoutonGo = Button(self.Mafenetre, text ='Normal', command = self.New_game_normal)
		BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		BoutonGo = Button(self.Mafenetre, text ='Hard', command = self.New_game_hard)
		BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		BoutonGo = Button(self.Mafenetre, text ='Standard Rules', command = self.New_game_Standard)
		BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		if self.boardSize > 6:
			BoutonGo = Button(self.Mafenetre, text ='Pro Rules', command = self.New_game_Pro)
			BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		if self.boardSize > 8:
			BoutonGo = Button(self.Mafenetre, text ='Longpro Rules', command = self.New_game_Longpro)
			BoutonGo.pack(side = TOP, padx = 10, pady = 10)

		# Création d'un widget Button (bouton Quitter)
		BoutonQuitter = Button(self.Mafenetre, text ='Quit', command = self.Mafenetre.destroy)
		BoutonQuitter.pack(side = BOTTOM, padx = 10, pady = 20)

	def Undo(self):
		""" Aller chercher la bonne pierre pour les prises OMG """
		if len(self.Canevas.find_all()) > 39:
			self.stones = self.Canevas.find_all()[-1]
			self.Canevas.delete(self.stones)
			# print ("Suppression de stone (item" , self.stones ,")")
			# print (self.Canevas.find_all())

	def EffacerTout(self):
		""" Efface tous les cercles"""
		for y in range(self.game.size):
			for x in range(self.game.size):
				if self.id_table[(y,x)] != 0:
					self.Canevas.delete(self.id_table[(y,x)])
		self.id_table = np.zeros((self.game.size, self.game.size), dtype=int)		


	def create_piece(self, position, value):
		r = 20
		u = 10
		y,x = position
		y = (y + 1) * 50
		x = (x + 1) * 50
		if value == 1:
			return self.Canevas.create_oval(x-r, y-r, x+r, y+r, width=2, outline='white', fill='white')
		elif value == -1:
			return self.Canevas.create_oval(x-r, y-r, x+r, y+r, width=2, outline='black', fill='black')
		elif value == 2:
			return self.Canevas.create_oval(x-u, y-u, x+u, y+u, width=2, outline='green', fill='green')
		elif value == 3:
			return self.Canevas.create_oval(x-u, y-u, x+u, y+u, width=2, outline='yellow', fill='yellow')
		elif value == 4:
			return self.Canevas.create_oval(x-u, y-u, x+u, y+u, width=2, outline='orange', fill='orange')
		elif value == 5:
			return self.Canevas.create_oval(x-u, y-u, x+u, y+u, width=2, outline='red', fill='red')
		else:
			print ("error color")

	def play(self, event):
		""" Gestion de l'événement Clic gauche sur la zone graphique """
		# position du pointeur de la souris
		X = event.x
		Y = event.y
		r = 20
		if (X % 50 > 25):
			# print ("x :", int (X / 50) + 1)
			x = (int (X / 50) + 1) * 50
		else:
			# print ("x :", int (X / 50))
			x = (int (X / 50) * 50)
	
		if (Y % 50 > 25):
			# print ("y :", int (Y / 50) + 1)
			y = (int (Y / 50) + 1) * 50
		else:
			# print ("y :", int (Y / 50))
			y = (int (Y / 50)) * 50

		self.valid_mooves = self.game.valid_moves(self.node)
		print ("Humain x :", int (x / 50-1), " y :", int (y / 50-1))

		if 0 <= int (y / 50-1) < self.game.size and 0 <= int (x / 50-1) < self.game.size and not self.game.end(self.node):
			child = self.game.player_move(self.node,( int(y/50-1) , int(x/50-1) ))
			
			if child != None:
				#la position est bonne, l'humain peux jouer
				if not self.vs_IA:
					for i in range(4):
						self.Canevas.delete(self.suggestion[i])
				for j in range(self.game.size):
					for i in range(self.game.size):
						if self.node.board[(j,i)] != child.board[(j,i)]:
							if child.board[(j,i)] != 0:
								self.id_table[(j,i)] = self.create_piece((j,i), child.board[(j,i)])
							else:
								self.Canevas.delete(self.id_table[(j,i)])

				# test_id = self.Canevas.create_oval(x-r, y-r, x+r, y+r, width=2, outline='black', fill='black')
				# print(type(test_id))

				self.node = child

				print(self.node.value)

				# time.sleep(0.5)
				if self.game.end(self.node):
					# self.game.print_node(self.node)
					if self.node.value == -np.inf:
						print("Black Win")
						showinfo("End of Game", "Black Win")
					elif self.node.value == np.inf:
						print("White Win")
						showinfo("End of Game", "White Win")
					else:
						print("Draw")
						showinfo("End of Game", "Draw")

				elif self.vs_IA:
					# methode pour faire calculer l'ia
					start = time.time()
					child = self.minimax.iterative_deepening(self.node)
					end = time.time()
					self.time = end - start
					self.sv.set(str(self.time))
					print("time: ", end - start)
					for j in range(self.game.size):
						for i in range(self.game.size):
							if self.node.board[(j,i)] != child.board[(j,i)]:
								if child.board[(j,i)] != 0:
									self.id_table[(j,i)] = self.create_piece((j,i), child.board[(j,i)])
								else:
									self.Canevas.delete(self.id_table[(j,i)])
					self.node = child

					#recup de la nouvelle map de jeux en ascii
					# self.game.print_node(self.node)
					#position jouer par l'ia
					print("IA :", self.node.position)
					self.turn = self.turn + 1
					print ("Tour numero: ", self.turn)
					self.tn.set(str(self.turn))

					y, x = self.node.position
					# print ("x de l'IA: ", x)
					# print ("y de l'IA: ", y)

					if self.game.end(self.node):
						if self.node.value == -np.inf:
							print("Black Win")
							showinfo("End of Game", "Black Win")
						elif self.node.value == np.inf:
							print("White Win")
							showinfo("End of Game", "White Win")
						else:
							print("Draw")
							showinfo("End of Game", "Draw")
				else:
					suggestions = self.minimax.suggestions(self.node)
					for i in range(4):
						self.suggestion[i] = self.create_piece(suggestions[i].position, 2 + i)
				self.cw.set(str(self.node.white_capture * 2))
				self.cb.set(str(self.node.black_capture * 2))
			else:
				print("Not a valid move")
		elif self.game.end(self.node):
			print ("GAME OVER")
		else:
			print("Play on Board plz")




if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('-b', '--board_size', action='store_true', help="change the board size")
	arg_parser.add_argument("files", metavar="file", nargs="*")
	args = arg_parser.parse_args()

	if args.board_size:
		while True:
			boardsize = input("Selectionnez la taille du plateau [5,19] : ")
			if 5 <= int(boardsize) <= 19:
				break
			else:
				print("Taille incorrecte. Veuillez selectionner une taille entre 5 et 19")
		board = Board(boardSize=int(boardsize))
	else:
		board = Board()
	toto = board.Canevas.bind('<Button-1>',board.play)
	board.Mafenetre.mainloop()










#Author: Toluwanimi Salako
from collections import defaultdict
import random
import sys
sys.path.append(r'\ConnectKSource_python')
import ConnectKSource_python.board_model as boardmodel

team_name = "PossiblySkynetAI" #TODO change me

class StudentAI():
	def __init__(self, player, state):
		self.last_move = state.get_last_move()
		self.model = state
		self.player = player
	def make_move(self, model, deadline):
		'''Write AI Here. Return a tuple (col, row)'''
		width = self.model.get_width()
		height = self.model.get_height()
		spaces = defaultdict(int)

		# for i in range(width):
		# 	for j in range(height):
		# 		spaces[(i,j)] = self.model.get_space(i, j)
		# print(self.player)
		# print(self.model.spaces_left)
		# print(deadline)
		# moves = [k for k in spaces.keys() if spaces[k] == 0]
		# return moves[random.randint(0, len(moves) - 1)]

		move = (self.minmax(self.model, -100, 100, 1).last_move)

		for i in range(0, 3):
			move = (self.minmax(self.model, -100, 100, i).last_move)

		# print(move)
		return move


	# possible take in a game state here
	def rateState(self, state):
		# length of the fucking thing
		# need to rewrite this since it is does not cover if an opponents piece is in the way
		# this was written in a motel room while I was watching over my sister-in-law
		# who is experiencing psychosis from withdrawls and staying awake for over
		# 24 hour periods of time to ensure that Alex isn't harmed since no center
		# has been able to take in Abby, please be forgiving of the level of optimization
		# given the current situation. Sorry for the rant comment.
		max_length = 0
		for i in range(state.get_width()):
			for j in range(state.get_height()):
				# change this a bit
				if(state.get_space(i, j) == self.player or state.get_space(i,j) == -self.player):
				# if(state.get_space(i, j) == 0):
					current_length_0 = 1
					current_length_1 = 1
					op_current_length_0 = 1
					op_current_length_1 = 1
					# get horizontal
					for offset in range(1, state.get_k_length()):
						# get left of the length
						if(i - offset >= 0 and state.get_space(i - offset, j) == state.get_space(i, j)):
							current_length_0 += 1

						if(i - offset >= 0 and state.get_space(i - offset, j) == -self.player):
							current_length_0 -= 1
							op_current_length_0 += 1

						if(i + offset < state.get_width() and state.get_space(i + offset, j) == state.get_space(i, j)):
							current_length_1 += 1

						if(i + offset < state.get_width() and state.get_space(i + offset, j) == -self.player):
							current_length_1 -= 1
							op_current_length_1 += 1

						max_length = max(max_length, current_length_0)
						max_length = max(max_length, current_length_1)

						# check for players in the way
						max_length = max(op_current_length_0, max_length)
						max_length = max(op_current_length_1, max_length)

					# get vertical
					current_length_0 = 1
					current_length_1 = 1
					op_current_length_0 = 1
					op_current_length_1 = 1
					for offset in range(1, state.get_k_length()):
						# get down
						if(j - offset >= 0 and state.get_space(i, j - offset) == state.get_space(i,j)):
							current_length_0 += 1

						if(j - offset >= 0 and state.get_space(i, j - offset) == -self.player):
							current_length_0 -= 1
							op_current_length_0 += 1

						# get up
						if(j + offset < state.get_height() and state.get_space(i, j + offset) == state.get_space(i,j)):
							current_length_1 += 1

						if(j + offset < state.get_height() and state.get_space(i, j + offset) == -self.player):
							current_length_1 -= 1
							op_current_length_1 += 1

						max_length = max(max_length, current_length_0)
						max_length = max(max_length, current_length_1)
						# check for players in the way
						max_length = max(op_current_length_0, max_length)
						max_length = max(op_current_length_1, max_length)

					# get left diagonal
					current_length_0 = 1
					current_length_1 = 1
					op_current_length_0 = 1
					op_current_length_1 = 1
					for offset in range(1, state.get_k_length()):
						# get left_down
						if(i - offset >= 0 and j - offset >= 0 and state.get_space(i - offset, j - offset) == state.get_space(i,j)):
							current_length_0 += 1

						if(i - offset >= 0 and j - offset >= 0 and state.get_space(i - offset, j - offset) == -self.player):
							current_length_0 -= 1
							op_current_length_0 += 1

						# get left_up
						if(i + offset < state.get_width() and j + offset < state.get_height() and state.get_space(i + offset, j + offset) == state.get_space(i,j)):
							current_length_1 += 1

						if(i + offset < state.get_width() and j + offset < state.get_height() and state.get_space(i + offset, j + offset) == -self.player):
							current_length_1 -= 1
							op_current_length_1 += 1


						max_length = max(max_length, current_length_0)
						max_length = max(max_length, current_length_1)
						# check for players in the way
						max_length = max(op_current_length_0, max_length)
						max_length = max(op_current_length_1, max_length)


					# get right diagonal
					current_length_0 = 1
					current_length_1 = 1
					op_current_length_0 = 1
					op_current_length_1 = 1
					for offset in range(1, state.get_k_length()):
						# get right_down
						if(i - offset >= 0 and j - offset >= 0 and state.get_space(i - offset, j - offset) == state.get_space(i,j)):
							current_length_0 += 1

						if(i - offset >= 0 and j - offset >= 0 and state.get_space(i - offset, j - offset) == -self.player):
							current_length_0 -= 1
							op_current_length_0 += 1

						if(i + offset < state.get_width() and j + offset < state.get_height() and state.get_space(i + offset, j + offset) == state.get_space(i,j)):
							current_length_1 += 1

						if(i + offset < state.get_width() and j + offset < state.get_height() and state.get_space(i + offset, j + offset) == -self.player):
							current_length_1 -= 1
							op_current_length_1 += 1

						max_length = max(max_length, current_length_0)
						max_length = max(max_length, current_length_1)
						# check for players in the way
						max_length = max(op_current_length_0, max_length)
						max_length = max(op_current_length_1, max_length)

		return max_length

	def minmax(self, state, alpha, beta, depth):
		# do minmax here
		if depth == 0:
			return state

		else:
			return self.maximize(state, alpha, beta, depth - 1)

		# print("minmax")

	def minimize(self, state, alpha, beta, depth):
		# minimize here
		# base case
		if depth == 0:
			return state

		else:
			levels_min = 1000
			min_state = state
			# generate next states
			new_level = self.generate_next_level(alpha, beta, state)
			for new_state in new_level:
				rating = self.rateState(self.maximize(new_state, alpha, beta, depth - 1))
				# check this later
				if(levels_min >= rating):
					# print("inside the minimizing if")
					levels_min = rating
					min_state = new_state
					beta = min(rating, beta)
					if(beta <= alpha):
						# print("prunning triggered min")
						break

			return min_state

	def maximize(self, state, alpha, beta, depth):
		# minimize here
		# base case
		if depth == 0:
			return state

		else:
			levels_max = -1000
			max_state = state
			# generate next states

			new_level = self.generate_next_level(alpha, beta, state)
			for new_state in new_level:
				rating = self.rateState(self.minimize(new_state, alpha, beta, depth - 1))
				if(levels_max <= rating):
					levels_max = rating
					max_state = new_state
					alpha = max(rating, alpha)
					if(beta <= alpha):
						# print("prunning triggered max")
						break

			return max_state

	def generate_next_level(self, alpha, beta, state):
		# if gravity show here
		states_generated = []
		if(state.gravity_enabled()):
			# print("with gravity")
			for w in range(state.get_width()):
				if(state.get_space(w, state.get_height() - 1) == 0):
					new_state = state.place_piece((w, new_state.get_height() - 1), self.player)
					rating = self.rateState(new_state)
					# if(rating <= alpha and rating >= beta):
					states_generated.append(new_state)

		else:
			for w in range(state.get_width()):
				for h in range(state.get_height()):
					if(state.get_space(w,h) == 0):
						new_state = state.place_piece((w,h), self.player)
						rating = self.rateState(new_state)
						states_generated.append(new_state)

		return states_generated



'''===================================
DO NOT MODIFY ANYTHING BELOW THIS LINE
==================================='''

is_first_player = False
deadline = 0
model = None

ai_piece = 1
human_piece = -1
no_piece = 0

def make_ai_shell_from_input():
	'''
	Reads board state from input and returns the move chosen by StudentAI
	DO NOT MODIFY THIS
	'''
	global is_first_player
	global model
	global deadline
	ai_shell = None
	begin =  "makeMoveWithState:"
	end = "end"

	go = True
	while (go):
		mass_input = input().split(" ")
		if (mass_input[0] == end):
			sys.exit()
		elif (mass_input[0] == begin):
			#first I want the gravity, then number of cols, then number of rows, then the col of the last move, then the row of the last move then the values for all the spaces.
			# 0 for no gravity, 1 for gravity
			#then rows
			#then cols
			#then lastMove col
			#then lastMove row.
			#then deadline.
			#add the K variable after deadline.
			#then the values for the spaces.
			#cout<<"beginning"<<endl;
			gravity = int(mass_input[1])
			col_count = int(mass_input[2])
			row_count = int(mass_input[3])
			last_move_col = int(mass_input[4])
			last_move_row = int(mass_input[5])

			#add the deadline here:
			deadline = -1
			deadline = int(mass_input[6])
			k = int(mass_input[7])
			#now the values for each space.


			counter = 8
			#allocate 2D array.
			model = boardmodel.BoardModel(col_count, row_count, k, gravity)
			count_own_moves = 0

			for col in range(col_count):
				for row in range(row_count):
					model.pieces[col][row] = int(mass_input[counter])
					if (model.pieces[col][row] == ai_piece):
						count_own_moves += model.pieces[col][row]
					if (not model.pieces[col][row] == no_piece):
						model.spaces_left -= 1
					counter+=1

			if (count_own_moves % 2 == 0):
				is_first_player = True

			model.last_move = (last_move_col, last_move_row)
			ai_shell = StudentAI(1 if is_first_player else 2, model)

			return ai_shell
		else:
			print("unrecognized command", mass_input)
		#otherwise loop back to the top and wait for proper _input.
	return ai_shell

def return_move(move):
	'''
	Prints the move made by the AI so the wrapping shell can input it
	DO NOT MODIFY THIS
	'''
	made_move = "ReturningTheMoveMade";
	#outputs made_move then a space then the row then a space then the column then a line break.
	print(made_move, move[0], move[1])

def check_if_first_player():
	global is_first_player
	return is_first_player

if __name__ == '__main__':
	'''
	DO NOT MODIFY THIS
	'''
	global deadline
	print ("Make sure this program is ran by the Java shell. It is incomplete on its own. :")
	go = True
	while (go): #do this forever until the make_ai_shell_from_input function ends the process or it is killed by the java wrapper.
		ai_shell = make_ai_shell_from_input()
		moveMade = ai_shell.make_move(model, deadline)
		return_move(moveMade)
		del ai_shell
		sys.stdout.flush()

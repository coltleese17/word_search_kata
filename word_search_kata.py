import sys
import pandas as pd

def check_letter_match(current_letter,search_letter):
	if current_letter == search_letter:
		return True
	else:
		return False

def continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction):

	while (check_letter_match(letter_grid[coord_x][coord_y], word[letter_index])):

		coordinates.append((coord_x,coord_y))

		if (letter_index == (len(word) - 1 )):
			return coordinates

		direction_x, direction_y = direction

		coord_x += direction_x
		coord_y += direction_y

		letter_index +=1	

	return False


def check_all_directions(coord_x,coord_y,letter_index,word,letter_grid):
	default_false_value = False

	#all methods return a list of coordinates for a found word, or False

	south_value = search_south(coord_x,coord_y,letter_index,word,letter_grid)
	if (south_value):
		return south_value

	east_value = search_east(coord_x,coord_y,letter_index,word,letter_grid)
	if (east_value):
		return east_value

	west_value = search_west(coord_x,coord_y,letter_index,word,letter_grid)
	if (west_value):
		return west_value	

	north_value = search_north(coord_x,coord_y,letter_index,word,letter_grid)
	if (north_value):
		return north_value

	south_east_value = search_south_east(coord_x,coord_y,letter_index,word,letter_grid)
	if (south_east_value):
		return south_east_value

	south_west_value = search_south_west(coord_x,coord_y,letter_index,word,letter_grid)
	if (south_west_value):
		return south_west_value			

	north_west_value = search_north_west(coord_x,coord_y,letter_index,word,letter_grid)
	if (north_west_value):
		return north_west_value		

	north_east_value = search_north_east(coord_x,coord_y,letter_index,word,letter_grid)
	if (north_east_value):
		return north_east_value			
	
	return default_false_value		

def search_east(coord_x,coord_y, letter_index, word,letter_grid):
	coordinates = [(coord_x,coord_y)]

	direction = (0,1)
	coord_y += 1
	letter_index += 1

	try:
		
		final_coordinates = continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction)
		if (final_coordinates):
			return final_coordinates	
		return False

	except (KeyError,IndexError):
	 	return False	

def search_south(coord_x,coord_y, letter_index, word,letter_grid):
	coordinates = [(coord_x,coord_y)]

	direction = (1,0)
	coord_x += 1
	letter_index += 1

	try:
		final_coordinates = continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction)
		if (final_coordinates):
			return final_coordinates
		return False

	except (KeyError,IndexError):
	 	return False	 	

def search_west(coord_x,coord_y, letter_index, word,letter_grid):
	coordinates = [(coord_x,coord_y)]

	direction = (0,-1)
	coord_y += -1
	letter_index += 1

	try:

		final_coordinates = continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction)
		if (final_coordinates):
			return final_coordinates

		return False

	except (KeyError,IndexError):
	 	return False	 	 

def search_north(coord_x,coord_y, letter_index, word,letter_grid):
	coordinates = [(coord_x,coord_y)]

	direction = (-1,0)
	coord_x += -1
	letter_index += 1

	try:
		final_coordinates = continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction)
		if (final_coordinates):
			return final_coordinates

		return False

	except (KeyError,IndexError):
	 	return False	 

def search_north_west(coord_x,coord_y, letter_index, word,letter_grid):
	coordinates = [(coord_x,coord_y)]

	direction =(-1,-1)

	coord_x += -1
	coord_y += -1 
	letter_index += 1

	try:
		final_coordinates = continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction)
		if (final_coordinates):
			return final_coordinates

		return False

	except (KeyError,IndexError):
	 	return False		 			 	 		

def search_south_west(coord_x,coord_y, letter_index, word,letter_grid):
	coordinates = [(coord_x,coord_y)]

	direction = (1,-1)

	coord_x += 1
	coord_y += -1 
	letter_index += 1

	try:
		final_coordinates = continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction)
		if (final_coordinates):
			return final_coordinates
		return False

	except (KeyError,IndexError):
	 	return False	

def search_south_east(coord_x,coord_y, letter_index, word,letter_grid):
	coordinates = [(coord_x,coord_y)]

	direction = (1,1)

	coord_x += 1
	coord_y += 1 
	letter_index += 1

	try:
		final_coordinates = continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction)
		if (final_coordinates):
			return final_coordinates
	
		return False

	except (KeyError,IndexError):
	 	return False	 			 			 	 			 	

def search_north_east(coord_x,coord_y, letter_index, word,letter_grid):
	coordinates = [(coord_x,coord_y)]

	direction = (-1,1)

	coord_x += -1
	coord_y += 1 
	letter_index += 1

	try:
		final_coordinates = continue_searching_in_this_direction(coord_x,coord_y, letter_index, word, letter_grid, coordinates, direction)
		if (final_coordinates):
			return final_coordinates	

		return False

	except (KeyError,IndexError):
	 	return False	 			 			 	 			 	 			


def main(text_file):
	with open(text_file, "r") as tf:

		word_list = tf.readline().strip().split(",")

		letter_grid = pd.read_csv(tf, header = None)

		letter_index = 0

		print word_list
		print letter_grid

		matches = {}

		for word in word_list:
			for coord_x in letter_grid:
				for coord_y in letter_grid:

					if (check_letter_match(letter_grid[coord_x][coord_y], word[letter_index])):

					 	word_coordinates = check_all_directions(coord_x,coord_y,letter_index, word,letter_grid)

					 	if (word_coordinates):
					 		matches[word] = word_coordinates
		print matches
		return matches			 		
					 			
if __name__ == '__main__':
	text_file = sys.argv[-1]
	main(text_file)
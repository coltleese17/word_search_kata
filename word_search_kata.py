import sys
import pandas as pd

def check_letter_match(current_letter,search_letter):
	if current_letter == search_letter:
		return True
	else:
		return False

def check_all_directions(x,y,letter_index,word,letter_grid):
	default_false_value = False

	#all methods return a list of coordinates for a found word, or False

	south_value = search_south(x,y,letter_index,word,letter_grid)
	if (south_value):
		return south_value

	east_value = search_east(x,y+1,letter_index,word,letter_grid)
	if (east_value):
		return east_value

	west_value = search_west(x,y,letter_index,word,letter_grid)
	if (west_value):
		return west_value	

	north_value = search_north(x,y,letter_index,word,letter_grid)
	if (north_value):
		return north_value

	south_east_value = search_south_east(x,y,letter_index,word,letter_grid)
	if (south_east_value):
		return south_east_value

	south_west_value = search_south_west(x,y,letter_index,word,letter_grid)
	if (south_west_value):
		return south_west_value			

	north_west_value = search_north_west(x,y,letter_index,word,letter_grid)
	if (north_west_value):
		return north_west_value		

	north_east_value = search_north_east(x,y,letter_index,word,letter_grid)
	if (north_east_value):
		return north_east_value			
	
	return default_false_value		

def search_east(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	y += 1
	letter_index += 1

	try:
		
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			if (letter_index == (len(word) - 1 )):
				return coordinates

			y += 1
			letter_index +=1	

		return False

	except (KeyError,IndexError):
	 		return False	

def search_south(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	x += 1
	letter_index += 1

	try:
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			if (letter_index == (len(word) - 1 )):
				return coordinates

			x += 1
			letter_index +=1	

		return False

	except (KeyError,IndexError):
	 		return False	 	

def search_west(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	y -= 1
	letter_index += 1

	try:
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			if (letter_index == (len(word) - 1 )):
				return coordinates

			y -= 1
			letter_index +=1	

		return False

	except (KeyError,IndexError):
	 		return False	 	 

def search_north(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	x -= 1
	letter_index += 1

	try:
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			if (letter_index == (len(word) - 1 )):
				return coordinates

			x -= 1
			letter_index +=1	

		return False

	except (KeyError,IndexError):
	 		return False	 

def search_north_west(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	x -= 1
	y -= 1 
	letter_index += 1

	try:
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			if (letter_index == (len(word) - 1 )):
				return coordinates

			x -= 1
			y -= 1
			letter_index +=1	

		return False

	except (KeyError,IndexError):
	 		return False		 			 	 		

def search_south_west(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	x += 1
	y -= 1 
	letter_index += 1

	try:
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			if (letter_index == (len(word) - 1 )):
				return coordinates

			x += 1
			y -= 1
			letter_index +=1	

		return False

	except (KeyError,IndexError):
	 		return False	

def search_south_east(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	x += 1
	y += 1 
	letter_index += 1

	try:
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			if (letter_index == (len(word) - 1 )):
				return coordinates


			x += 1
			y += 1
			letter_index +=1	
	
		return False

	except (KeyError,IndexError):
	 		return False	 			 			 	 			 	

def search_north_east(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	x -= 1
	y += 1 
	letter_index += 1

	try:
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			if (letter_index == (len(word) - 1 )):
				return coordinates

			x -= 1
			y += 1
			letter_index +=1	

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
			for x in letter_grid:
				for y in letter_grid:

					if (check_letter_match(letter_grid[x][y], word[letter_index])):

					 	word_coordinates = check_all_directions(x,y,letter_index, word,letter_grid)

					 	if (word_coordinates):
					 		matches[word] = word_coordinates
		print matches
		return matches			 		
					 			
if __name__ == '__main__':
	text_file = sys.argv[-1]
	main(text_file)
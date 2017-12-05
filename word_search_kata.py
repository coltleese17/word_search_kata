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

#only returns the coordinates of a found word in a list of tuples, or false.
def search_east(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	#change the position 1 column east and look to match the next letter
	y += 1
	letter_index += 1

	try:
		#continue while matches are being found
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			#if we reach the last letter, we know we've found the word, return the coordinates
			if (letter_index == (len(word) - 1 )):
				return coordinates

			#change the position 1 column east and look for the next letter
			y += 1
			letter_index +=1	

		#if no matches	
		return False

	#exceptions for if the search goes off the grid
	except Exception as e:
			#print "Out Of Bounds!"
	 		#print e
	 		return False	

#only returns the coordinates of a found word in a list of tuples, or false.
def search_south(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	#change the position 1 row south and look to match the next letter
	x += 1
	letter_index += 1

	try:
		#continue while matches are being found
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			#if we reach the last letter, we know we've found the word, return the coordinates
			if (letter_index == (len(word) - 1 )):
				return coordinates

			#change the position 1 row south and look for the next letter
			x += 1
			letter_index +=1	

		#if no matches	
		return False

	#exceptions for if the search goes off the grid
	except Exception as e:
			#print "Out Of Bounds!"
	 		#print e
	 		return False	 	

#only returns the coordinates of a found word in a list of tuples, or false.
def search_west(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	#change the position 1 column west and look to match the next letter
	y -= 1
	letter_index += 1

	try:
		#continue while matches are being found
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			#if we reach the last letter, we know we've found the word, return the coordinates
			if (letter_index == (len(word) - 1 )):
				return coordinates

			#change the position 1 column west and look for the next letter
			y -= 1
			letter_index +=1	

		#if no matches	
		return False

	#exceptions for if the search goes off the grid
	except Exception as e:
			#print "Out Of Bounds!"
	 		#print e
	 		return False	 	 

#only returns the coordinates of a found word in a list of tuples, or false.
def search_north(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	#change the position 1 row north and look to match the next letter
	x -= 1
	letter_index += 1

	try:
		#continue while matches are being found
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			#if we reach the last letter, we know we've found the word, return the coordinates
			if (letter_index == (len(word) - 1 )):
				return coordinates

			#change the position 1 row north and look for the next letter
			x -= 1
			letter_index +=1	

		#if no matches	
		return False

	#exceptions for if the search goes off the grid
	except Exception as e:
			#print "Out Of Bounds!"
	 		#print e
	 		return False	 

#only returns the coordinates of a found word in a list of tuples, or false.
def search_north_west(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	#change the position 1 row north and 1 column west and look to match the next letter
	x -= 1
	y -= 1 
	letter_index += 1

	try:
		#continue while matches are being found
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			#if we reach the last letter, we know we've found the word, return the coordinates
			if (letter_index == (len(word) - 1 )):
				return coordinates

			#change the position 1 row north and 1 column west look for the next letter
			x -= 1
			y -= 1
			letter_index +=1	

		#if no matches	
		return False

	#exceptions for if the search goes off the grid
	except Exception as e:
			#print "Out Of Bounds!"
	 		#print e
	 		return False		 			 	 		

#only returns the coordinates of a found word in a list of tuples, or false.
def search_south_west(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	#change the position 1 row south and 1 column west and look to match the next letter
	x += 1
	y -= 1 
	letter_index += 1

	try:
		#continue while matches are being found
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			#if we reach the last letter, we know we've found the word, return the coordinates
			if (letter_index == (len(word) - 1 )):
				return coordinates

			#change the position 1 row south and 1 column west look for the next letter
			x += 1
			y -= 1
			letter_index +=1	

		#if no matches	
		return False

	#exceptions for if the search goes off the grid
	except Exception as e:
			#print "Out Of Bounds!"
	 		#print e
	 		return False	

#only returns the coordinates of a found word in a list of tuples, or false.
def search_south_east(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	#change the position 1 row south and 1 column east and look to match the next letter
	x += 1
	y += 1 
	letter_index += 1

	try:
		#continue while matches are being found
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			#if we reach the last letter, we know we've found the word, return the coordinates
			if (letter_index == (len(word) - 1 )):
				return coordinates

			#change the position 1 row south and 1 column east look for the next letter
			x += 1
			y += 1
			letter_index +=1	

		#if no matches	
		return False

	#exceptions for if the search goes off the grid
	except Exception as e:
			#print "Out Of Bounds!"
	 		#print e
	 		return False	 			 			 	 			 	

#only returns the coordinates of a found word in a list of tuples, or false.
def search_north_east(x,y, letter_index, word,letter_grid):
	coordinates = [(x,y)]

	#change the position 1 row north and 1 column east and look to match the next letter
	x -= 1
	y += 1 
	letter_index += 1

	try:
		#continue while matches are being found
		while (check_letter_match(letter_grid[x][y], word[letter_index])):

			coordinates.append((x,y))

			#if we reach the last letter, we know we've found the word, return the coordinates
			if (letter_index == (len(word) - 1 )):
				return coordinates

			#change the position 1 row north and 1 column east look for the next letter
			x -= 1
			y += 1
			letter_index +=1	

		#if no matches	
		return False

	#exceptions for if the search goes off the grid
	except Exception as e:
			#print "Out Of Bounds!"
	 		#print e
	 		return False	 			 			 	 			 	 			



def main(text_file):
	with open(text_file, "r") as tf:

		#pull in a list of words from the first line
		word_list = tf.readline().strip().split(",")

		#set the letter grid as a dataframe
		letter_grid = pd.read_csv(tf, header = None)

		print word_list
		print letter_grid

if __name__ == '__main__':
	# load in file from command line
	text_file = sys.argv[-1]
	main(text_file)
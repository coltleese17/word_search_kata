import sys
import pandas as pd

def check_letter_match(current_letter,search_letter):
	if current_letter == search_letter:
		return True
	else:
		return False

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
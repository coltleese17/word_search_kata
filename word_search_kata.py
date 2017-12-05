import sys
import pandas as pd

def check_letter_match(current_letter,search_letter):
	if current_letter == search_letter:
		return True
	else:
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
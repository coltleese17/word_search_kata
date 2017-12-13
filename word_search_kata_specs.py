import word_search_kata
import unittest

#word_search_kata.main('word-search-content.txt')

#simulating the letter grid
letter_grid_3x3 = [['t','h','e'], 
				   ['o','o','a'],
				   ['o','w','t']]

class wordSearchTDD(unittest.TestCase):

	def test_search_east(self):
		x = 0
		y = 0 
		letter_index = 0
		word = 'the' 
		coordinates = word_search_kata.search_east(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( [(0,0),(0,1),(0,2)] , coordinates)

	def test_search_east_searchword_too_long(self):
		x = 0 
		y = 0 
		letter_index = 0
		word = 'them' 
		coordinates = word_search_kata.search_east(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( False , coordinates)	

	def test_search_south(self):
		x = 0
		y = 0 
		letter_index = 0
		word = 'too' 
		coordinates = word_search_kata.search_south(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( [(0,0),(1,0),(2,0)] , coordinates)

	def test_search_west(self):
		x = 0
		y = 2 
		letter_index = 0
		word = 'eht' 
		coordinates = word_search_kata.search_west(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( [(0,2),(0,1),(0,0)] , coordinates)	

	def test_search_north(self):
		x = 2
		y = 0
		letter_index = 0
		word = 'oot' 
		coordinates = word_search_kata.search_north(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( [(2,0),(1,0),(0,0)] , coordinates)

	def test_search_north_west(self):
		x = 2
		y = 2
		letter_index = 0
		word = 'tot' 
		coordinates = word_search_kata.search_north_west(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( [(2,2),(1,1),(0,0)] , coordinates)	

	def test_search_south_west(self):
		x = 0
		y = 2
		letter_index = 0
		word = 'eoo' 
		coordinates = word_search_kata.search_south_west(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( [(0,2),(1,1),(2,0)] , coordinates)	

	def test_search_south_east(self):
		x = 0
		y = 0
		letter_index = 0
		word = 'tot' 
		coordinates = word_search_kata.search_south_east(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( [(0,0),(1,1),(2,2)] , coordinates)				

	def test_search_north_east(self):
		x = 2
		y = 0
		letter_index = 0
		word = 'ooe' 
		coordinates = word_search_kata.search_north_east(x,y,letter_index,word,letter_grid_3x3)
		self.assertEqual( [(2,0),(1,1),(0,2)] , coordinates)		

	def test_main_with_values_not_found_on_grid(self):
		output_of_full_program = word_search_kata.main('word-search-content-mock-with-searchwords-not-on-grid.txt')
		self.assertEqual( {}, output_of_full_program)

	def test_main_for_success(self):
		output_of_full_program = word_search_kata.main('word-search-content.txt')
		self.assertEqual( {'UHURA': [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
		 					'KHAN': [(5, 9), (5, 8), (5, 7), (5, 6)], 
		 					'SULU': [(3, 3), (2, 2), (1, 1), (0, 0)],
		 					'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
		 					'KIRK': [(4, 7), (3, 7), (2, 7), (1, 7)],
		 					'SPOCK': [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)]}, output_of_full_program)	


if __name__ == '__main__':
	unittest.main()		

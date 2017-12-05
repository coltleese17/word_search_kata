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

if __name__ == '__main__':
	unittest.main()		

# word_search_kata

Python solution and tests for the word search kata found here: https://github.com/PillarTechnology/kata-word-search/

To run from command line, enter:

`python word_search_kata.py [your-file]`

To run the tests, enter:

`python word_search_kata_specs.py`

A high level explanation of the algorithm is:
  * Search the 2d grid linearly for a letter that matches the first letter of the search word.

  * Once found, search in every direction for a letter that matches the second letter of the search word.
  * If a second match is found, search in that direction until the end of the word.
  <br>&nbsp;&nbsp;&nbsp;&nbsp; -If you reach the end of the word, return the coordinates of the word, else return false.
  
  * If a second match is not found, continue searching linearly. Repeat steps 2-3.
  
Coded in Python 2.7.13

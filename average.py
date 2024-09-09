"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""

import text_utils
import math

def average():
    file = open('sample.txt', 'r')
    lines = file.readlines()
    line_count = 0
    word_count = 0
    for line in lines:    
        line_count = line_count + 1
        word_count = word_count + text_utils.count_words(line)                        
    file.close()
    S2BA = word_count / line_count
    rounded_down = math.floor(S2BA)
    return(rounded_down)

print(f"Average words per line: {average()}")

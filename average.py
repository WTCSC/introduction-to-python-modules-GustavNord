# imports the modules to be able to use them
import text_utils
import math
# defines the function that will calculate the average number of words per line
def average():
# opens the sample.txt file in read mode
    file = open('sample.txt', 'r')
# reads all lines from the file
    lines = file.readlines()
# starts a count for how many lines and words
    line_count = 0
    word_count = 0
# goes through each line in the file
    for line in lines:    
# continues the count by adding 1 each time then closes the file
        line_count = line_count + 1
        word_count = word_count + text_utils.count_words(line)                        
    file.close()
# Adds a constant that stands for "Soon to be Average," which calculates the average number of words per line
    S2BA = word_count / line_count
# rounds the Soon to be Average number down
    rounded_down = math.floor(S2BA)
# returns the rounded down number
    return(rounded_down)
# prints: "Average words per line: average"
print(f"Average words per line: {average()}")

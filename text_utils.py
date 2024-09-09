# defines the function in this module
def count_chars(text):
# returns how long the text is
   return len(text) 

# defines another function in this module
def count_words(text):
# splits the texts into a list of words in a variable and then returns the amount of words
    num_of_words = text.split()
    return len(num_of_words)

# defines another function in this module
def count_sentences(text):
# counts how many ".", "!", and "?" there are
    dot_count = text.count('.')
    bang_count = text.count('!')
    questionmark_count = text.count('?')
# adds the total for each ".", "!", and "?" together and then returns that number
    sum_sentences = dot_count + bang_count + questionmark_count
    return(sum_sentences)
    
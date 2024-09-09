def count_chars(text):
   return len(text) 

def count_words(text):
    num_of_words = text.split()
    return len(num_of_words)

def count_sentences(text):
    dot_count = text.count('.')
    bang_count = text.count('!')
    questionmark_count = text.count('?')
    sum_sentences = dot_count + bang_count + questionmark_count
    return(sum_sentences)
    
from functools import reduce 
import re
def map_func(wc): 
    with open(file_name, 'r') as file: 
        lines = file.readlines() 
        words = [word.strip() for line in lines for word in line.split()] 
        return words 
def reduce_func(words): 
    word_count = {} 
    for word in words: 
        if word in word_count: 
            word_count[word] += 1 
        else: 
            word_count[word] = 1 
    return word_count 
def word_count(wc): 
    words = map_func(file_name) 
    word_count = reduce_func(words) 
    return word_count 
file_name = r'C:\Users\sivaj\OneDrive\Desktop\CRT\\wc.txt' 
word_count_result = word_count(file_name) 
print("Word count:") 
for word, count in word_count_result.items(): 
    print(f"{word}: {count}")

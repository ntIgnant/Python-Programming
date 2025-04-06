from collections import Counter
import pathlib


# Change this to "text" for the full book
file_name = "text.txt"

# Do not modify this part
with (pathlib.Path(__file__).parent / file_name).open("rt", encoding="utf-8") as f:
    text = f.read()

# print(text)
'''
Count which word appears how often and print the 20 most frequent words, and count
which character appears how often and print their relative frequencies (see also Zipf’s law)
'''

splited_text = text.lower().split() # split the words of the text (and convert all of them into lowercase)
# print(splited_text)

word_count_most = Counter(splited_text).most_common(20) # this will print the 20 most used words of the text (with their number of occurrences)
print(word_count_most)

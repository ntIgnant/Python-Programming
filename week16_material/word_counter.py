import collections
import pathlib

# Change this to "text" for the full book
file_name = "text_excerpt.txt"

# Do not modify this part
with (pathlib.Path(__file__).parent / file_name).open("rt", encoding="utf-8") as f:
    text = f.read()

# print(text)
'''
Count which word appears how often and print the 20 most frequent words, and count
which character appears how often and print their relative frequencies (see also Zipf’s law)
'''

collections.Counter()

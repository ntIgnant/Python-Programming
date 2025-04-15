from collections import Counter
from pathlib import Path


with Path("text.txt").open("rt") as file:
    content = file.read().lower().split() # this is for the text content to have a uniform format
    book_content = content # Creates a non-iterable variable (copy to reuse it)

word_count = Counter(book_content).most_common(20) # This will count the 20 most used words in the text

print(word_count)


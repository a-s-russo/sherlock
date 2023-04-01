import math
import os
import string
from collections import Counter

import matplotlib.pyplot as plt


#################
# DATA CLEANING #
#################

# Read in raw data as list of lines
def read_all_stories(path):
    text = []
    for _, _, files in os.walk(path):
        for file in files:
            with open(path + file) as f:
                for line in f:
                    text.append(line)
    return text


# Clean data and convert to list of words
def clean_text(text):
    cleaned_text = []
    for line in text:
        for word in line.split():
            word = word.lower().strip()  # Remove whitespace
            word = word.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
            if word != '\n' and word:  # Remove newline characters and empty strings
                cleaned_text.append(word)
    return cleaned_text


#################
# DATA PLOTTING #
#################

# Read in and clean Sherlock stories
stories = read_all_stories("C:/Users/asrus/PycharmProjects/sherlock/data/")
cleaned_stories = clean_text(stories)

# Generate word frequency data
word_counter = Counter(cleaned_stories)
word_counts = list(word_counter.values())
word_counts.sort(reverse=True)

# Generate plot data
x = [math.log10(word_counts.index(word) + 1) for word in word_counts]
y = [math.log10(word) for word in word_counts]

# Plot data
plt.plot(x, y, marker='o', linewidth=0)
plt.title("Word Frequency of Sherlock Holmes' Stories\nLog-log Scale")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.show()

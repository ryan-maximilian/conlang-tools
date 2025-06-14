# Word of the Day
# 
# Simply picks a random entry from a list
# 
# Included is the original Swadesh list from Wikipedia
# https://en.wikipedia.org/wiki/Swadesh_list#Swadesh_100_original_final_list

import random

with open('wotd.txt') as f:
    lines_in_file = 0
    for line in f:
        lines_in_file += 1
    f.seek(0)
    todays_word = random.randrange(lines_in_file) + 1
    for i, line in enumerate(f, start=1):
        if i == todays_word:
            print(line.strip())
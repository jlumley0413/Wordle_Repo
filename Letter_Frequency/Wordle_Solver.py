#Read large dictionary file and make second list of only 5-letter words
five_letter_list = list()
with open("Dictionary_58110.txt") as f:
    for word in f:
        x = word.rstrip("\n")
        if len(x) == 5:
            five_letter_list.append(x)

f.close()

with open("Dictionary_58110.txt") as f:
    for word in f:
        x = word.rstrip("\n")
        if len(x) == 4:
            x = x + 's'
            if x in five_letter_list:
                five_letter_list.remove(x)

f.close()

import numpy as np
import random
import time
import matplotlib.pyplot as plt

from Full_Run import Full_Run
from Initialization import Initialization
from Score_System4b import Score_System4b
from GYB_checker import GYB_checker
from MasterTracker import MasterTracker 

##EVENTUALLY - get rid of plural words

Cumulative_Results = []
for i in range(100):
    Cumulative_Results = Full_Run(Cumulative_Results, five_letter_list)

print(Cumulative_Results)

Score3 = Cumulative_Results
print(np.mean(Score3))

avg_guesses = np.mean(Score3)

from collections import Counter
num_bins = len(list(Counter(Cumulative_Results).keys()))

# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=Cumulative_Results, bins=num_bins, color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Guesses')
plt.ylabel('Frequency')
plt.title(f'Score3 Guesses: Mean = {avg_guesses}')

maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()

# NEXT STEPS
## Put plotting functionality in
## Alternative score systems - don't reward multiple letter usage. Award points for most common letter placement
## Interact with Wordle - be able to input guess and output recommended word
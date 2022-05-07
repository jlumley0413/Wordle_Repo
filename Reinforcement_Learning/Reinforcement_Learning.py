import random
import pandas as pd
import numpy as np
from Explore import Explore

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

learning_rate = 0.04
print(len(five_letter_list))

#print(correct_word)

# The q-table is a matrix with all words ("actions") down the rows, and the % of dictionary remaining in the columns. It is divided into
#100%, 40-99%, 16-39%, 4-15%, 1-4%, <1%

Q_table = pd.DataFrame(np.zeros((len(five_letter_list),7)), columns=["100%","40-99%","16-39%","6-15%","1-5%","0.25-1%","<0.25%"], index=five_letter_list)
Q_table_count = pd.DataFrame(np.zeros((len(five_letter_list),7)), columns=["100%","40-99%","16-39%","6-15%","1-5%","0.25-1%","<0.25%"], index=five_letter_list)
#Q_table["100%"]["aback"]=1

#print(Q_table)

for count in range(1000000):
    correct_word = five_letter_list[random.randrange(len(five_letter_list))]
    Q_table, Q_table_count = Explore(correct_word, five_letter_list,Q_table,learning_rate, Q_table_count)
    if count%10000 == 0:
        print(count/10000)
print(Q_table)

Q_avg = Q_table / Q_table_count
Q_avg.to_csv(r'C:\Users\Joshua Lumley\Documents\Python_with_Ian\Wordle\Reinforcement_Learning\Q_table.txt', header=None, index=five_letter_list, sep=' ', mode='a')
Q_table_count.to_csv(r'C:\Users\Joshua Lumley\Documents\Python_with_Ian\Wordle\Reinforcement_Learning\Q_table.txt', header=None, index=five_letter_list, sep=' ', mode='a')
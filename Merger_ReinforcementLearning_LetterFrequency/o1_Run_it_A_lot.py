#Letter_Frequency Goal was to run the Wordle_Solver 100 times to get different ratios of y:z and see if any ratio gets us a better score.
#Best y:z ratio was <0.25.
#New goal is to combine the Q-table elimination method with the optimal ratio and see if we get improved results

import pandas as pd
from o2_Wordle_Solver_Multi_Run import Multi_Wordle_Solver

#Read in exploit's Q_table
Q_table = pd.read_csv('Merger_ReinforcementLearning_LetterFrequency/Q_table.txt', sep=" ", header=None, index_col = 0)
Q_table.columns = ["100%","40-99%","16-39%","6-15%","1-5%","0.25-1%","<0.25%"]
Q_table = Q_table.fillna(0)

#How many times to run this?
Ratio_y_to_z = 0.2
Ratio_Q_to_LetterFreq = [0.01, 0.1, 0.25, 0.5, 1, 2, 4, 10, 100]

results = {}

for i in Ratio_Q_to_LetterFreq:
    average = Multi_Wordle_Solver(Q_table, i, Ratio_y_to_z)
    print(i)
    results[i] = average

print(results)

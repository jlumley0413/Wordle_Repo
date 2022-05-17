import numpy as np

from o3_Full_Run import Full_Run

def Multi_Wordle_Solver(Q_table, ratio_q_to_LF, ratio_y_to_z):
    #print("Made it to Multi Wordle Solver \n")
    Cumulative_Results = []
    for i in range(1000):
        Cumulative_Results = Full_Run(Cumulative_Results, Q_table, ratio_q_to_LF, ratio_y_to_z)
        #print("in Multi Wordle Solver's loop: #",i)
    Score3 = Cumulative_Results
    avg_guesses = np.mean(Score3)

    return avg_guesses
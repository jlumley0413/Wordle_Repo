from o4_Initialization import Initialization
from o5_Score_System5 import Score_System5
from o7_GYB_checker import GYB_checker

def Full_Run(Cumulative_Results, Q_table, ratio_q_to_LF, ratio_y_to_z = 0.2):
    original_num_words = len(Q_table.index)
    remaining_Q_words, Results, guess, correct_word = Initialization(Q_table, original_num_words, ratio_q_to_LF, ratio_y_to_z)
    
    #print(correct_word," is the correct word \n")
    while guess != correct_word:
        if len(Results) > 0: 
            guess = Score_System5(remaining_Q_words, original_num_words, ratio_q_to_LF, ratio_y_to_z)
        remaining_Q_words, colors = GYB_checker(remaining_Q_words,guess,correct_word)
        Results.append([guess, colors])
        #print(guess, " Is my guess \n")

    
    #print("Last Run: \n",*Results, sep='\n')
    
    Cumulative_Results.append(len(Results))
    #print(Cumulative_Results)
    return Cumulative_Results
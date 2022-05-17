from o5_Score_System5 import Score_System5
import random

def Initialization(Q_table, ratio_q_to_LF, ratio_y_to_z, original_num_words):
    #Initializing the run
    remaining_Q_words = Q_table.copy()
    Results = []
    guess = Score_System5(remaining_Q_words, original_num_words, ratio_q_to_LF, ratio_y_to_z)

    correct_word = remaining_Q_words.index[random.randrange(len(remaining_Q_words.index))]
    
    return remaining_Q_words, Results, guess, correct_word
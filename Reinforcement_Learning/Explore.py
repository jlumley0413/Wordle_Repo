import random
from GYB_checker import GYB_checker
from Update_Q_table import Update_Q_table

def Explore(correct_word, five_letter_list,Q_table,learning_rate,Q_table_count):
    guess = []
    remaining_words = five_letter_list.copy()
    original_length = len(five_letter_list)

    while guess != correct_word:
        old_length = len(remaining_words)
        guess = remaining_words[random.randrange(old_length)]
        #print(guess)

        remaining_words, ignore_letters, colors = GYB_checker(guess, correct_word, remaining_words)
        #print(remaining_words)
        new_length = len(remaining_words)

        #print(elimination)
        if new_length != 1:
            elimination = 1 - (new_length-1) / (old_length-1)
            bucket = old_length / original_length
            Q_table, Q_table_count = Update_Q_table(Q_table,guess,elimination,bucket,learning_rate, Q_table_count)
            #Q_table["100%"][guess]=1
            #print(Q_table)
    return Q_table, Q_table_count
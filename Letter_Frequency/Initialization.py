from Score_System4b import Score_System4b
import random

def Initialization(five_letter_list, ratio = []):
    #Initializing the run
    possible_word_list = five_letter_list.copy()
    ignore_letters = []
    Results = []
    guess, y = Score_System4b(possible_word_list, ignore_letters)

    correct_word = five_letter_list[random.randrange(len(five_letter_list))]
    
    return possible_word_list, ignore_letters, Results, guess, y, correct_word
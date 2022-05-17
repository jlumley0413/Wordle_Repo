from Initialization import Initialization
from Score_System4b import Score_System4b
from GYB_checker import GYB_checker
from MasterTracker import MasterTracker

def Full_Run(Cumulative_Results, five_letter_list, ratio = 0.2):
    possible_word_list, ignore_letters, Results, guess, y, correct_word = Initialization(five_letter_list, ratio)
    #print(correct_word)
    while guess != correct_word:
        #print(guess)
        guess, y = Score_System4b(possible_word_list, ignore_letters, ratio)
        possible_word_list, ignore_letters, colors = GYB_checker(guess,correct_word, possible_word_list)
        Results = MasterTracker(guess, colors, Results)
    
    #print("Last Run: \n",*Results, sep='\n')
    
    Cumulative_Results.append(len(Results))
    #print(Cumulative_Results)
    return Cumulative_Results
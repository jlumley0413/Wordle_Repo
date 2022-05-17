import numpy as np
import random
import time
import matplotlib.pyplot as plt

from Full_Run import Full_Run
from Initialization import Initialization
from Score_System4b import Score_System4b
from GYB_checker import GYB_checker
from MasterTracker import MasterTracker 

def Multi_Wordle_Solver(five_letter_list, ratio):

    Cumulative_Results = []
    for i in range(100):
        Cumulative_Results = Full_Run(Cumulative_Results, five_letter_list, ratio)

    Score3 = Cumulative_Results
    avg_guesses = np.mean(Score3)

    return avg_guesses
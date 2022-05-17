import numpy as np
from o6_Read_Q_table2 import Read_Q_table2

def Score_System5(remaining_Q_words, original_num_words, ratio_q_to_LF, ratio_y_to_z = 0.2):
    #Function that counts the "score" of each available word
    #Score System 5 is a modification of score system 4b that gives equal weight to letter frequency in a word and to its location, and also accepts
    # ratios of the q-table of predictive % elimination ability to letter frequency
    #For any green letters, it zeros out that position in [y] only. Because both yellow and green letters are passed in ignore_letters, a different
    #method was used for this.
    
    points = []
    possible_words_list = list(remaining_Q_words.index)
    list_len = len(possible_words_list)
    #print(possible_words_list)
    #print("In Score_System5 ",list_len)

    y = np.zeros((26,5), dtype=int) #y is a 26x5 matrix that will hold how many times each letter is in each position
    for word in possible_words_list:
        for i in range(5):
            letter_val = ord(word[i])-96
            y[letter_val-1][i] += 1
    
    #here we zero any green letters
    for i in range(len(y)):
        for j in range(len(y[0])):
            if y[i][j] >= list_len:
                y[i][j] = 0

    #print(y)

    z = np.zeros(26, dtype = float) #z is a 26x1 matrix that will hold how many times each letter is in the possible_words_list
    for count in range(26):
        z[count] = sum(y[count,:])
    
    for word in possible_words_list:
        score = 0
        for i in range(5):
            first_letter_appearance = True
            if first_letter_appearance == True:
                score += y[ord(word[i])-97][i]
                score += (z[ord(word[i])-97])*ratio_y_to_z
        points.append(score) 
    
    if len(list(remaining_Q_words.index)) == 1:
        guess = remaining_Q_words.idxmax()['100%']
    else:
        points = points/max(points) #scaling all points so that the highest value in the table is 1.

        remaining_Q_words['yz_subscore'] = points
        Q_column_index = Read_Q_table2(list_len / original_num_words)

        remaining_Q_words['total_score'] = remaining_Q_words['yz_subscore'] + remaining_Q_words['100%']*ratio_q_to_LF
        #print(remaining_Q_words.head(15))
        guess = remaining_Q_words.idxmax()['total_score']
        #print("in 05 time to return guess: ", guess)
    return guess
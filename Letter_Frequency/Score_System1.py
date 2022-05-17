import numpy as np

def Score_System1(possible_words_list, ignore_letters):
    #Function that counts the "score" of each available word
    #Score System 1 = Alleged improvement over Score System 2.  Assigns 1 point for each time a letter appears in the possible word list
    #For any known green or yellow letter, it sets the value == 0.
    
    points = []
    
    y = np.zeros((26,5), dtype=int) #y is a 26x5 matrix that will hold how many times each letter is in each position
    for word in possible_words_list:
        for i in range(5):
            letter_val = ord(word[i])-96
            y[letter_val-1][i] += 1
    
    for letter in ignore_letters: #This code is not scoring letters we already know exist in the word
        y[ord(letter)-97][:] = 0
    
    z = np.zeros(26, dtype = int) #z is a 26x1 matrix that will hold how many times each letter is in the possible_words_list
    for count in range(26):
        z[count] = sum(y[count,:])

    for word in possible_words_list:
        score = 0
        for i in range(5):
            score += z[ord(word[i])-97]
        points.append(score)
    
    max_word_num = points.index(max(points))
    guess = possible_words_list[max_word_num]
    
    return guess, y
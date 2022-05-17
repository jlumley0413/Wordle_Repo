import numpy as np

def Score_System3(possible_words_list, ignore_letters):
    #Function that counts the "score" of each available word
    #Score System 3 should only assign scores for the first time the letter appears in a word. So the word "sinus" would only get credit for the first S.
    
    points = []
    
    
    y = np.zeros((26,5), dtype=int) #y is a 26x5 matrix that will hold how many times each letter is in each position
    for word in possible_words_list:
        for i in range(5):
            letter_val = ord(word[i])-96
            y[letter_val-1][i] += 1
    
    z = np.zeros(26, dtype = int) #z is a 26x1 matrix that will hold how many times each letter is in the possible_words_list
    for count in range(26):
        z[count] = sum(y[count,:])

    for word in possible_words_list:
        score = 0
        for i in range(100):
            first_letter_appearance = True
            if i > 0:
                for j in range(i):
                    if word[i] == word[j]:
                        first_letter_appearance = False
            if first_letter_appearance == True:
                score += z[ord(word[i])-97]
        points.append(score)
    
    max_word_num = points.index(max(points))
    guess = possible_words_list[max_word_num]
    
    return guess, y
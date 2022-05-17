import numpy as np

def Score_System4b(possible_words_list, ignore_letters, ratio = 0.2):
    #Function that counts the "score" of each available word
    #Score System 4 is an attempt to give points for guessing words with more optimal letter position. So (e.g.) words with an h as their second letter
    #will earn more points than those with h as their 3rd letter.
    #For any green letters, it zeros out that position in [y] only. Because both yellow and green letters are passed in ignore_letters, a different
    #method was used for this.
    
    #This is a slight change to Score_System 4 where we add points for the y value of position + z/5.
    
    points = []
    
    list_len = len(possible_words_list)
    #print(list_len)
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

    z = np.zeros(26, dtype = int) #z is a 26x1 matrix that will hold how many times each letter is in the possible_words_list
    for count in range(26):
        z[count] = sum(y[count,:])
    
    for word in possible_words_list:
        score = 0
        for i in range(5):
            first_letter_appearance = True
            if first_letter_appearance == True:
                score += y[ord(word[i])-97][i]
                score += (z[ord(word[i])-97])*ratio
        points.append(score)
        #print(word,": ", score)
   
    #print(z)
    #print(y)
    #print(possible_words_list)

    max_word_num = points.index(max(points))
    guess = possible_words_list[max_word_num]
    
    return guess, y
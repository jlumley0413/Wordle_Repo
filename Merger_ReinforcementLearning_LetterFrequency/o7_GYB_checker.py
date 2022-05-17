def GYB_checker(remaining_Q_words, guess, correct_word):
    #Comparing word to guess word
    #print("Entered the checker\n")
    #print("Guess = ",guess)
    #print("Correct word = ", correct_word)
    nonGreen_list = [0, 1, 2, 3, 4]
    Nongray_list = []
    colors = ['-','-','-','-','-'] #used to store the colors of the guessed word
    
    #Removing words where greens don't align
    for i in range(5):
        word_removal_list = []
        if guess[i] == correct_word[i]:
            nonGreen_list.remove(i)
            Nongray_list.append(i)
            colors[i] = 'G'
            for word in remaining_Q_words.index:
                if word[i] != guess[i]:
                    word_removal_list.append(word)
        remaining_Q_words = remaining_Q_words.drop(word_removal_list, axis = 0)  

    #Find Yellows
    Yellow_list = []
    Gray_list = []
 
    checklist = nonGreen_list.copy()

    for i in nonGreen_list:
        done = 1
        for j in checklist:
            if guess[i] == correct_word[j] and done:
                Yellow_list.append(i)
                colors[i] = 'Y'
                done = 0
                checklist.remove(j)
        if done:
            Gray_list.append(i)
        else:
            Nongray_list.append(i)

    #Removing words where guessed word YELLOW is a GREEN with a possible remaining word
    for i in Yellow_list:
        word_removal_list = []
        for checked_word in remaining_Q_words.index:
            if guess[i] == checked_word[i]:
                word_removal_list.append(checked_word)
        remaining_Q_words = remaining_Q_words.drop(word_removal_list, axis = 0)  

    #Removing words where guessed word YELLOW does not exist in remaining word
    for i in Yellow_list:
        word_removal_list = []
        for checked_word in remaining_Q_words.index:
            letter_exists = 0
            for j in nonGreen_list:
                if guess[i] == checked_word[j]:
                    letter_exists = 1
            if letter_exists == 0:
                word_removal_list.append(checked_word)
        remaining_Q_words = remaining_Q_words.drop(word_removal_list, axis = 0)  

    #Removing words where grays exist
    for i in Gray_list:
                    #print('\n\n\n\n i = ',i,'\n\n\n')
        word_removal_list = []
        for checked_word in remaining_Q_words.index:
            done = 1
            for j in checklist:                                  # COULD BE NONGREENLIST
                if guess[i] == checked_word[j] and done:
                    word_removal_list.append(checked_word)
                    done = 0
        remaining_Q_words = remaining_Q_words.drop(word_removal_list, axis = 0)  

    return remaining_Q_words, colors

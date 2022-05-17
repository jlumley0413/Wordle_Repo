def GYB_checker(guess, correct_word, possible_word_list):
    #Comparing word to guess word

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
            for word in possible_word_list:
                if word[i] != guess[i]:
                    word_removal_list.append(word)
            for word2 in word_removal_list:
                possible_word_list.remove(word2)

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
        for checked_word in possible_word_list:
            if guess[i] == checked_word[i]:
                word_removal_list.append(checked_word)
        for word2 in word_removal_list:
            possible_word_list.remove(word2)

    #Removing words where guessed word YELLOW does not exist in remaining word
    for i in Yellow_list:
        word_removal_list = []
        for checked_word in possible_word_list:
            letter_exists = 0
            for j in nonGreen_list:
                if guess[i] == checked_word[j]:
                    letter_exists = 1
            if letter_exists == 0:
                word_removal_list.append(checked_word)
        for word2 in word_removal_list:
            possible_word_list.remove(word2)     

    #Removing words where grays exist
    for i in Gray_list:
                    #print('\n\n\n\n i = ',i,'\n\n\n')
        word_removal_list = []
        for checked_word in possible_word_list:
            done = 1
            for j in checklist:                                  # COULD BE NONGREENLIST
                if guess[i] == checked_word[j] and done:
                    word_removal_list.append(checked_word)
                    done = 0
        for word2 in word_removal_list:
            possible_word_list.remove(word2)
    
    #Convert Nongray_list into a list of letters not to be scored
    ignore_letters = []
    for i in Nongray_list:
        ignore_letters.append(guess[i])
                    #print(ignore_letters)
    #print(guess,": ", colors)
    return possible_word_list, ignore_letters, colors
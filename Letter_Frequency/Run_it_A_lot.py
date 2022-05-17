#Goal is to run the Wordle_Solver 100 times to get different ratios of y:z and see if any ratio gets us a better score 

from Wordle_Solver_Multi_Run import Multi_Wordle_Solver

#Read large dictionary file and make second list of only 5-letter words
five_letter_list = list()
with open("Letter_Frequency/Dictionary_58110.txt") as f:
    for word in f:
        x = word.rstrip("\n")
        if len(x) == 5:
            five_letter_list.append(x)

f.close()

with open("Letter_Frequency/Dictionary_58110.txt") as f:
    for word in f:
        x = word.rstrip("\n")
        if len(x) == 4:
            x = x + 's'
            if x in five_letter_list:
                five_letter_list.remove(x)

f.close()

#How many times to run this?
Ratio_y_to_z = [0.01, 0.1, 0.25, 0.5, 1, 2, 4, 10, 100]

results = {}
for i in Ratio_y_to_z:
    average = Multi_Wordle_Solver(five_letter_list, i)
    print(i)
    results[i] = average

print(results)

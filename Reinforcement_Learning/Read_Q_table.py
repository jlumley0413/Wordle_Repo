import numpy as np

def Read_Q_table(percent_remaining, remaining_Q_words):
    guess = []
    print("Made it to Read_Q_table")
    if percent_remaining == 1:
        Q_column_index = "100%"
    elif percent_remaining >= 0.4:
        Q_column_index = "40-99%"
    elif percent_remaining >= 0.16:
        Q_column_index = "16-39%"
    elif percent_remaining >= 0.064:
        Q_column_index = "6-15%"
    elif percent_remaining >= 0.01:
        Q_column_index = "1-5%"
    elif percent_remaining >= 0.0025:
        Q_column_index = "0.25-1%"
    else:
        Q_column_index = "<0.25%"

    guess = remaining_Q_words.idxmax()[Q_column_index]

    return guess
def Update_Q_table(Q_table,guess,elimination,bucket,learning_rate, Q_table_count):
    if bucket == 1:
        Q_column_index = "100%"
    elif bucket >= 0.4:
        Q_column_index = "40-99%"
    elif bucket >= 0.16:
        Q_column_index = "16-39%"
    elif bucket >= 0.064:
        Q_column_index = "6-15%"
    elif bucket >= 0.01:
        Q_column_index = "1-5%"
    elif bucket >= 0.0025:
        Q_column_index = "0.25-1%"
    else:
        Q_column_index = "<0.25%"

    #Q_table[Q_column_index][guess] = (1-learning_rate)*Q_table[Q_column_index][guess]+learning_rate*elimination
    Q_table[Q_column_index][guess] += elimination
    Q_table_count[Q_column_index][guess] +=1

    return Q_table, Q_table_count


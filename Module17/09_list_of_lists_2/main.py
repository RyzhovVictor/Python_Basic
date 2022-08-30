nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

disclose = [finish_value for next_list in nice_list
            for next_value in next_list for finish_value in next_value]

print(disclose)

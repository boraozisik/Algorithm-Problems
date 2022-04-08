"""
Given an array of 0s and 1s, find the index of 0 to be replaced with 1
to get longest continuous sequence of 1s.

"""



def findIndexofZero(list):
    max_count = 0
    max_index = -1

    prev_zero_index = -1
    count_zeros = 0


    for i in range(len(list)):


        if list[i] == 1:
            count_zeros = count_zeros + 1

        else:

            count_zeros = i - prev_zero_index


            prev_zero_index = i


        if count_zeros > max_count:
            max_count = count_zeros
            max_index = prev_zero_index


    return max_index


print(findIndexofZero([0,0,1,0,1,1,1,0,1,1]))
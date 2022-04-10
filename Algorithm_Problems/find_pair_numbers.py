"""
The function will find the pair numbers those sum equal to K value, and returns them as String.
Example [9, 6, 5, 7, 1, 3, 2, 4, 10, 8] K=16 returns "(9,7)" and "(10,6)".
"""


def solution(list, k):
    final_list = []
    for i in range(len(list)):
        for j in list:
            if (j + list[i] == k and j != list[i]) and ([list[i], j] not in final_list):
                final_list.append([j, list[i]])

    print(final_list)


list = [9,6,5,7,1,3,2,4,10,8]

solution(list, 16)
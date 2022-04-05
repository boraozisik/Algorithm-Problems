"""
Colleen is turning n years old! Therefore, she has n candles of various heights on her cake, and candle i has height. Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the height for each individual candle, find and print the number of candles she can successfully blow out.

Input Format

The first line contains a single integer, , denoting the number of candles on the cake. The second line contains space-separated integers, where each integer describes the height of candle .

Output Format

Print the number of candles Colleen blows out on a new line.
"""


def solution(nCandle, arrOfHeights):

    max_candles = []
    max_value = max(arrOfHeights)

    for i in range(nCandle):
        if arrOfHeights[i] == max_value:
            max_candles.append(arrOfHeights[i])

    print(max_candles)


solution(5, [3,6,7,1,7])
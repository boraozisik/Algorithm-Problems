import re


def solution(shelf_length, books):

    total_width = 0
    total_shelf = 0
    shelf_count = 0

    for i in books:
        str = i
        temp = re.compile("([0-9]+)([a-zA-Z]+)")
        res = temp.match(str).groups()
        total_width += int(res[0])

    for i in range(len(shelf_length)):
        shelf_count += 1
        total_shelf += shelf_length[i]
        if total_shelf >= total_width:
            break

    print(shelf_count - 1)


shelfLength = [150, 150, 300, 150, 150]

books = {
    "70gameofthrones",
    "76dancingwiththestarman",
    "99RocketLaunchers",
    "75DontPanic!",
    "105AnElectricCarAnd400mKilometers"
}

solution(shelfLength, books)
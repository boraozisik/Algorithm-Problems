"""
Given a string containing only digits, restore it by returning valid IP address.

Example:

    given: "25525522235"
    return: "255.255.222.35"

"""



def solution(ip_address):
    ip_address_list = list(ip_address)
    arranged_list = []
    arranged_string = ""

    for i in range(int(len(ip_address_list) / 3)):
        for j in range(3):
            arranged_list.append(ip_address_list[0])
            ip_address_list.remove(ip_address_list[0])
        arranged_list.append(".")



    for i in arranged_list:
        arranged_string += i

    for i in ip_address_list:
        arranged_string += i



    print(arranged_string)


solution("25525522235")
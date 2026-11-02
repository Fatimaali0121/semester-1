# code example on slide 10
def test(x, intList):           # takes the og list and directly applyes the change on it
    intList.append(x)
    return intList


list1 = [2, 4, 6, 8]
print(list1)             # [2, 4, 6, 8]
print(test(500, list1))  # [2, 4, 6, 8, 500]
print(list1)             # [2, 4, 6, 8, 500]


# code example on slide 11
def test2(x, intList):          # creates a copy and do the changes on it and it saves the og list
    temp_list2 = intList.copy()
    temp_list2.append(x)
    return temp_list2


list2 = [1, 2, 3, 4]
print(list2)             # [1, 2, 3, 4]
print(test2(5, list2))   # [1, 2, 3, 4, 5]
print(list2)             # [1, 2, 3, 4]

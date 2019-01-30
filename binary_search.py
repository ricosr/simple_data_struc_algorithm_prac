# -*- coding:utf-8 -*-

# 二分查找


def binary_search(ls, target):
    low = 0
    high = len(ls)-1
    while low <= high:
        mid = (low + high)//2
        if ls[mid] == target:
            return mid
        elif ls[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "not exist"


ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
print(binary_search(ls, target))

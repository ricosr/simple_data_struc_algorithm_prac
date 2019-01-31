# -*- coding:utf-8 -*-

# 索引查找


class IndexType:
    def __init__(self, key, link):
        self.key = key
        self.link = link


def index_search(index_ls, data_ls, index_len, key):
    i = 0
    while i < index_len and key > index_ls[i].key:
        i += 1
    if i == index_len:
        return -1
    else:
        j = index_ls[i].link
        while key != data_ls[j] and j < index_ls[i+1].link:
            j += 1
        if key == data_ls[j]:
            return j
        else:
            return -2


if __name__ == '__main__':
    data_list = [2, 3, 4, 5, 6,
                 10, 7, 8, 9, 11,
                 12, 44, 33, 22, 41,
                 77, 66, 55, 88, 65,
                 99, 98, 97, 89, 90,
                 188, 166, 160]
    index_list = [IndexType(6, 0), IndexType(10, 5), IndexType(44, 10), IndexType(88, 15), IndexType(99, 20),
                  IndexType(188, 25), IndexType(-1, 28)]
    print(index_search(index_list, data_list, 6, 22))
    print(index_search(index_list, data_list, 6, 2))
    print(index_search(index_list, data_list, 6, 6))
    print(index_search(index_list, data_list, 6, 77))
    print(index_search(index_list, data_list, 6, 65))
    print(index_search(index_list, data_list, 6, 188))
    print(index_search(index_list, data_list, 6, 160))



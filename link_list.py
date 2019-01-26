# -*- coding:utf-8 -*-

# 双向链表：有头结点，所有操作头结点不占下标，头结点下一个节点是0节点

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


class Link:
    def __init__(self):
        head_node = Node(-1)
        self.head = head_node

    def add_node(self, value):    # 链表后加入新节点
        tmp_point = self.head
        while True:
            if not tmp_point.right:
                new_node = Node(value)
                tmp_point.right = new_node
                new_node.left = tmp_point
                break
            else:
                tmp_point = tmp_point.right

    def insert_node(self, index, value):    # 按下标插入新节点
        tmp_point = self.head
        for i in range(index):
            tmp_point = tmp_point.right
        new_node = Node(value)
        temp = tmp_point.right
        tmp_point.right = new_node
        new_node.right = temp

        new_node.left = tmp_point
        temp.left = new_node

    def delete_node(self, index):    # 按下标删除节点
        tmp_point = self.head
        for i in range(index):
            tmp_point = tmp_point.right
        temp_node = tmp_point.right
        tmp_point.right = temp_node.right
        temp_node.right.left = tmp_point
        del(temp_node)

    def search_node(self, value):    # 按值查找下标
        tmp_point = self.head
        index = -1
        while True:
            tmp_point = tmp_point.right
            index += 1
            if tmp_point:
                if tmp_point.value == value:
                    return index
            else:
                return "no find index"

    def change_value(self, index, value):    # 按下标改值
        tmp_point = self.head
        for i in range(index+1):
            tmp_point = tmp_point.right
        tmp_point.value = value

    def print_link(self):    # 正向遍历
        tmp_point = self.head
        while True:
            if tmp_point.right:
                print(tmp_point.value)
                tmp_point = tmp_point.right
            else:
                print(tmp_point.value)
                break

    def invert_print(self):    # 反向遍历
        tmp_point = self.head
        while True:
            tmp_point = tmp_point.right
            if not tmp_point.right:
                break
        while True:
            if tmp_point.left:
                print(tmp_point.value)
                tmp_point = tmp_point.left
            else:
                print(tmp_point.value)
                break


if __name__ == '__main__':
    print("build:")
    link = Link()
    link.add_node(1)
    link.add_node(2)
    link.add_node(3)
    link.add_node(5)
    link.add_node(6)

    print("****************************")
    link.print_link()
    print("--------------")
    link.invert_print()
    print("****************************")

    print("insert:")
    link.insert_node(3, 4)
    link.insert_node(0, 0)
    link.print_link()
    print("--------------")
    link.invert_print()
    print("****************************")

    print("delete:")
    link.delete_node(4)
    link.delete_node(0)

    link.print_link()
    print("--------------")
    link.invert_print()
    print("****************************")

    print("search:")
    print(link.search_node(0))
    print(link.search_node(3))
    print("****************************")

    print("change:")
    link.change_value(4, 9)
    link.change_value(0, 8)
    link.print_link()










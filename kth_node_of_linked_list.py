# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2022/1/2 5:11 下午
@File: kth_node_of_linked_list.py
求链表的倒数第k个元素
'''


def find_kth_element(head, k):
    """
    找倒数第k个元素
    :param head: LinkedList
    :param k: int
    :return:
    """
    fast = slow = head
    while k != 0:
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    return slow
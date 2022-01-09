# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2022/1/2 4:59 下午
@File: middle_of_linkedList.py
'''


def middle_linked_list(head):
    """
    找链表的中点
    :param head:
    :return:
    """
    fast = slow = head
    while fast is not None and slow is not None:
        fast = fast.next.next
        slow = slow.next
    # slow就在中间
    return slow
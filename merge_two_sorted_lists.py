"""
MERGE TWO SORTED LISTS

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        travel = merged = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                travel.next = list1
                travel = travel.next
                list1 = list1.next
            elif list2.val <=  list1.val:
                travel.next = list2
                travel = travel.next
                list2 = list2.next

        if list1 or list2:
            travel.next = list1 if list1 else list2

        return merged.next
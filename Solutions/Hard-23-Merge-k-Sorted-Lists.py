"""
    23. Merge k Sorted Lists
    https://leetcode.com/problems/merge-k-sorted-lists/
"""

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper function to create a linked list from a Python list
def create_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# Helper function to convert a linked list to a Python list for printing
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            _, index, node = heapq.heappop(heap)

            # result's linked list - building node list from heap
            curr.next = node
            curr = node

            # check if value exists in popped node's next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, index, node))

        return dummy.next


# Create input linked lists
lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6]),
]

# Solve and print the result
print(f"Input lists: {[linked_list_to_list(lst) for lst in lists]}")
print(f"Output: {linked_list_to_list(Solution().mergeKLists(lists))}")

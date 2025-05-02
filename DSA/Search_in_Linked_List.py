# Search in Linked List
# https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/0
# Given a linked list of n nodes and a key, the task is to check if the key is present in the linked list or not.
# Example:
# Input: n = 4, key = 3
# 1->2->3->4
# Output: true
# Explanation: 3 is present in Linked List, so the function returns true.
# Constraint:
# 1 <= n <= 105
# 1 <= key <= 105


class Solution:
    def searchKey(self, n, head, key):
        #Code here
        curr=head
        while curr:
            if curr.data==key:
                return True
            curr=curr.next
        return False
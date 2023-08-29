'''
Remove loop from singly linked list if exists.

Given a linked list of N nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X(1-based index).
If the link list does not have any loop, X=0.
Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.


Example 1:

Input:
N = 3
value[] = {1,3,4}
X = 2
Output: 1
Explanation: The link list looks like
1 -> 3 -> 4
     ^    |
     |____|
A loop is present. If you remove it
successfully, the answer will be 1.

Link to the problem: https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1?page=1&sortBy=submissions


'''

'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''


class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        if not head:
            return
        p = head
        q = head

        while p and q:
            if not q.next:
                return
            p = p.next
            q = q.next.next
            if p == q:
                break
        if p == q:
            p = head
            while p != q:
                p = p.next
                q = q.next
            while q.next != p:
                q = q.next
            q.next = None

        return
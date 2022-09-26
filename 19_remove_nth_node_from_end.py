# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        node = self
        arr = [node.val]
        while node.next is not None:
            node = node.next
            arr.append(node.val)
        return "[{}]".format(", ".join(map(str, arr)))

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 1
        node = head
        values = [node.val]
        while node.next is not None:
            count += 1
            node = node.next
            values.append(node.val)


        if len(values) == 1 and n == 1:
            return None

        values.pop(-n)


        if len(values) == 0:
            return None

        lastnode = ListNode(val = values[-1], next=None)
        for v in reversed(values[0:-1]):
            newnode = ListNode(v,lastnode)
            lastnode = newnode
                        
        return lastnode

def test_solution():
    assert Solution().removeNthFromEnd(head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))), n = 2) == [1,2,3,5]
    # assert Solution().removeNthFromEnd(head = ListNode(1), n = 1) == []




    
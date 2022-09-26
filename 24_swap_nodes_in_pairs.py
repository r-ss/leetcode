# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/swap-nodes-in-pairs/

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


class LinkedListHelper:
    def length(self, node: ListNode) -> int:
        if node == None:
            return 0
        count = 1
        if node.next == None:
            return count
        while node.next is not None:
            count += 1
            node = node.next
        return count
    
    def values(self, node: ListNode) -> List:
        values = []
        if node == None:
            return values
        while node.next is not None:
            values.append(node.val)
            node = node.next
        values.append(node.val)
        return values

    def construct(self, values: Optional[List]) -> ListNode:
        if not values:
            return None
        if len(values) == 1:
            return ListNode(val = values[0], next=None)
        node = ListNode(val = values[-1], next=None)
        for v in reversed(values[0:-1]):
            newnode = ListNode(v,node)
            node = newnode
        return node

class Solution:
    def swapPairs(self, head: Optional[ListNode] = None) -> Optional[ListNode]:

        values = LinkedListHelper().values(head)
        # print("values:", values)

        if len(values) == 0:
            return None

        if len(values) == 1:
            return head

        new = []
        for n in range(len(values)):
            val = values[n]
            if (n % 2) == 0:
                # even
                new.insert(n, val)
            else:
                # odd
                new.insert(n-1, val)

        node = LinkedListHelper().construct(new)
        print(node)
        return node

def test_solution():
    assert str(Solution().swapPairs(head = ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))) == str(LinkedListHelper().construct([2,1,4,3]))
    assert str(Solution().swapPairs(head = ListNode(0,ListNode(4,ListNode(9,ListNode(2)))))) == str(LinkedListHelper().construct([4,0,2,9]))
    assert str(Solution().swapPairs(head = ListNode())) == str(LinkedListHelper().construct([]))
    assert str(Solution().swapPairs(head = ListNode(1))) == str(LinkedListHelper().construct([1]))



    
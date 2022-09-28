# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/reverse-nodes-in-k-group/

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

    def construct(self, values: Optional[List] = None) -> ListNode:
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        values = LinkedListHelper().values(head)

        if len(values) == 0:
            return None

        if len(values) == 1:
            return head

        new = []

        def divide_array_to_chunks(l, n):
            # looping till length l
            for i in range(0, len(l), n):
                yield l[i:i + n]

        chunks = list(divide_array_to_chunks(values, k))

        for i in range(len(chunks)):
            chunk = chunks[i]
            if len(chunk) >= k:
                for j in reversed(chunk):
                    new.append(j)
            else:
                for j in chunk:
                    new.append(j)

        node = LinkedListHelper().construct(new)
        return node

def test_solution():
    assert str(Solution().reverseKGroup(head = LinkedListHelper().construct([1,2,3,4,5]), k = 2)) == str(LinkedListHelper().construct([2,1,4,3,5]))
    assert str(Solution().reverseKGroup(head = LinkedListHelper().construct([1,2,3,4,5]), k = 3)) == str(LinkedListHelper().construct([3,2,1,4,5]))
    # assert str(Solution().reverseKGroup(head = ListNode())) == str(LinkedListHelper().construct())
    # assert str(Solution().reverseKGroup(head = ListNode(1))) == str(LinkedListHelper().construct([1]))



    
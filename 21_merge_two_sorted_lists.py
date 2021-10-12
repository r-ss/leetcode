# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, a:ListNode, b:ListNode) -> ListNode:
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

def test_solution():
    assert Solution().mergeTwoLists(a = ListNode(1,ListNode(2,ListNode(4))), b = ListNode(1,ListNode(3,ListNode(4)))) == [1,1,2,3,4,4]
    # assert Solution().mergeTwoLists(a = [], b = []) == []
    # assert Solution().mergeTwoLists(a = [], b = [0]) == [0]

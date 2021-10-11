# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/add-two-numbers/

# from typing import NewType
# Optional = NewType('Optional', object)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1, l2):
        
        # print(ListNode)
        
        integers = []
        for node in [l1, l2]:
            s = str(node.val)
            while node.next is not None:
                node = node.next
                s += str(node.val)
            integers.append(int(s[::-1]))

            
        # print(integers[0] + integers[1])
        
        s = str(integers[0] + integers[1])
        
        # print(s)
        
        
        # node = ListNode(list(s)[0])
        # node.next = ListNode(list(s)[1])
        # appender = None
        head = None
        for index, i in enumerate(reversed(list(s))):
            # print(index, i)
            
            if head is None:
                node = ListNode(list(s)[0])
            else:
                node = ListNode(list(s)[index], head)
                
            head = ListNode(list(s)[index], head)
                
            # # node_next = ListNodeExt(val = int(i))
            # if index == len(list(s)):
            #     appender = ListNode(list(s)[index-1])
            # else:
            #     appender = ListNode(list(s)[index])
            # node.next = appender
            
            # new = ListNodeExt(int(i))
            # node.insert(node, new)
            # node.insert(list(s)[index])
            
        # node_next = ListNode(len(list(s)))
        # node.next = node_next
            
            
        
        # LL.insert(3)
        # print(node)
        return(node)


def test_solution():
    l1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 3)))
    l2 = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(val = 4)))

    assert Solution().addTwoNumbers(l1, l2).val == str(7)
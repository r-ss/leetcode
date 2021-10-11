# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        def median(l):
            half = len(l) // 2
            l.sort()
            if not len(l) % 2:
                return (l[half - 1] + l[half]) / 2.0
            return l[half]
        
        arr = nums1 + nums2
        # print(arr)
        
        return median(arr)
        

def test_solution():

    assert Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2]) == 2.00000
    assert Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]) == 2.50000
    assert Solution().findMedianSortedArrays(nums1 = [0,0], nums2 = [0,0]) == 0.00000
    assert Solution().findMedianSortedArrays(nums1 = [], nums2 = [1]) == 1.00000
    assert Solution().findMedianSortedArrays(nums1 = [2], nums2 = []) == 2.00000
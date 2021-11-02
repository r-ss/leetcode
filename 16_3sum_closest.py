# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums, target) -> int:

        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]

        for i in range(1, n - 1):

            l, c, r = 0, i, n - 1
            while l < r:

                if l >= c:
                    break
                if r <= c:
                    break

                sum = nums[l] + nums[c] + nums[r]

                if sum == target:
                    return sum
                

                # print('sum', i, ' (', nums[l],  nums[c], nums[r], ') ', sum)

                if abs(sum - target) < abs(ans - target):
                    ans = sum

                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1

        return ans

        # def takeClosest(num, collection):
        #     return min(collection,key=lambda x:abs(x-num))


        # sums = []


        # l = len(nums)
        # for a in range(l):
        #     for b in range(a+1, l):
        #         for c in range(b+1, l):
        #             diff = nums[a] + nums[b] + nums[c]
        #             sums.append(diff)


        # # print(sums)

        # return takeClosest(target, sums)
        

n = [-12,-10,32,88,4,64,-57,-57,62,0,74,95,-23,10,-21,80,-74,36,-54,17,-97,-8,-86,43,95,-76,-18,-43,-43,31,-64,-96,-66,-42,-88,-44,-6,-2,16,-6,90,-45,52,48,-6,58,21,7,-18,73,-75,-90,-34,6,3,94,26,33,-92,73,-25,-67,16,-99,-90,-40,19,-78,-53,-36,28,82,33,66,-27,54,-34,-30,27,51,-32,-13,-52,37,-41,-95,68,56,23,57,25,-69,-65,43,-60,-41,-51,77,44,-6,-19,-87,-43,-54,97,82,-54,-13,82,43,-83,100,37,-34,-56,-65,-7,27,-25,-82,91,-76,46,-29,-78,69,-21,25,-10,71]
        
def test_solution():
    assert Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1) == 2
    assert Solution().threeSumClosest(nums = [0,0,0], target = 1) == 0
    assert Solution().threeSumClosest(nums = n, target = 129) == 129


    


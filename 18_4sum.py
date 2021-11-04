# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums, target):

        nums.sort()
        l = len(nums)
        # ans = nums[0] + nums[1] + nums[2] + nums[3]
        ans = []


        


        for i in range(l-3):

            for j in range(l-3):

                print('new loops')
                
                a, b, c, d = i, i+1, l-(j+2), l-(j+1)

                while b < c:

                    av, bv, cv, dv = nums[a], nums[b], nums[c], nums[d]
                    s = sum([av,bv,cv,dv])

                    # ok, fail = ', <<<< MATCH', ''
                    # print( f'sum {s} abcd {a, b, c, d} values {av, bv, cv, dv} target {target}{ ok if s == target else fail }' )

                    if s > target:
                        c-=1
                        continue
                    if s < target:
                        b+=1
                        continue
                    
                    if s == target:
                        ans.append([av,bv,cv,dv])

                    b+=1


        def make_unique(original_list):
            ''' removes dublicates from list '''
            unique_list = []
            [unique_list.append(obj) for obj in original_list if obj not in unique_list]
            return unique_list

        print( make_unique(ans) )
        # list(set()) to remove dublicates because set is guaranteed to not have duplicates.
        return make_unique(ans)
        

        

def test_solution():
    assert Solution().fourSum(nums = [-2,-1,0,0,1,2], target = 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    assert Solution().fourSum(nums = [2,2,2,2,2], target = 8) == [[2,2,2,2]]
    assert Solution().fourSum(nums = [-3,-1,0,2,4,5], target = 2) == [[-3,-1,2,4]]
    assert Solution().fourSum(nums = [-3,-1,0,2,4,5], target = 0) == [[-3,-1,0,4]]
    assert Solution().fourSum(nums = [-3,-2,-1,0,0,1,2,3], target = 0) == [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
                                                                        # [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],                       [-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
                                                                        #                                       0,3,5,6    1, 2,3,7

    


# -2 -1 0 0 1 2
#  a  b     c d
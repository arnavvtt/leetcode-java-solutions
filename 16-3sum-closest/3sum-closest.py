import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        max_diff=math.inf
        result_sum = 0

        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                curr_sum=nums[i]+nums[left]+nums[right]
                diff=abs(curr_sum-target)
                if diff < max_diff:
                    max_diff=diff
                    result_sum=curr_sum
                if curr_sum==target:
                    return curr_sum
                elif curr_sum<target:
                    left+=1
                else:
                    right-=1
        return result_sum      
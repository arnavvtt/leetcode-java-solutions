class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        window_sum=0
        min_length=float('inf')
        # 
        k=0
        for i in range (n):
            window_sum=window_sum+nums[i]
            while window_sum>= target:
                curr_length = i-k+1
                min_length= min(min_length, curr_length)
                window_sum-= nums[k]
                k+=1
        if min_length==float('inf'):
            return 0
        
        return min_length

        
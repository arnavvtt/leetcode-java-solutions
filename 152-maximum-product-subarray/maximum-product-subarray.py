class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        i=0
        bestending=nums[0]
        ans=nums[0]
        worstending=nums[0]
        for i in range (1,len(nums)):
            i1=bestending*nums[i]
            i2=worstending*nums[i]
            i3=nums[i]

            bestending=max(i1,i2,i3)
            worstending=min(i1,i2,i3)
            ans=max(bestending,ans)
        return ans
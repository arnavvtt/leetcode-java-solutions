class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        subarrays = 0
        product=1
        first_index=0
        for i in range (len(nums)):
            product=product*nums[i]

            while product>=k:
                product = product /nums[first_index]
                first_index+=1

            window_length= i-first_index+1
            subarrays = subarrays + window_length
            
        return subarrays
        
        
      
    
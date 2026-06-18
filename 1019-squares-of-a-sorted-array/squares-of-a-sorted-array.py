class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]* n
        i= 0
        j=n-1
        k=n-1

        while i<=j:
            if abs(nums[i])>=abs(nums[j]):
                result[k] = nums[i]*nums[i]
                i=i+1
            else:
                result[k] = nums[j]*nums[j]
                j=j-1
            k=k-1   
        return result
            

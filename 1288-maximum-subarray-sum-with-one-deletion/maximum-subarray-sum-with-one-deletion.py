class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        a=arr[0]
        b=float('-inf')
        ans=arr[0]
        for i in range(1,len(arr)):
            x=arr[i]
            new_b = max(b + x, a)  # Purana a abhi available hai
            a = max(a + x, x)      # Ab a update hoga
            b = new_b              # Ab b update hoga
            ans=max(ans,a,b)
        return ans


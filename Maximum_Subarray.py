#leetcode ( Kadane's Algorithm )
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            cursum=cursum+nums[i]
            if(ans<cursum):
                ans=cursum
            if(cursum<0):
                cursum=0
        return ans
        
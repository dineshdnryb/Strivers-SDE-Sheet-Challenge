# Leetcode
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        idx=-1
        swap=-1
        swapval=1e9
        for i in range(n-2,-1,-1):
            if(nums[i]<nums[i+1]):
                idx=i
                break
        if(idx==-1):
            for i in range(n//2):
                nums[i],nums[n-1-i]=nums[n-1-i],nums[i]
        else:
            for i in range(idx+1,n):
                if(nums[i]>nums[idx]):
                    if(nums[i]<=swapval):
                        swap=i
                        swapval=nums[i]
            else:       
                nums[idx],nums[swap]=nums[swap],nums[idx]
                print(nums)
                for i in range((n-(idx+1))//2):
                    nums[idx+1+i],nums[n-1-i]=nums[n-1-i],nums[idx+1+i]

            

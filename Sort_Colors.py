# leetcode (sort 0,1,2 in place)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        left=0
        right=n-1
        mid=0
        while(mid<=right):
            if(nums[mid]==2):
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
            elif(nums[mid]==0):
                nums[mid],nums[left]=nums[left],nums[mid]
                left+=1
                mid+=1
            else:
                mid+=1
                

        
        
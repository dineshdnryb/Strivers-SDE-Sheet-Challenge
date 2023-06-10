# leetcode
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        ans=0
        minv=prices[0]
        for i in range(1,n):
            if(minv>prices[i]):
                minv=prices[i]
            if(minv<prices[i] and ans<prices[i]-minv):
                ans=prices[i]-minv
        return ans

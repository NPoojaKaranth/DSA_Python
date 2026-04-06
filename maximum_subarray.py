class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        summ=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            summ=max(summ,curr)
        return summ
            

        

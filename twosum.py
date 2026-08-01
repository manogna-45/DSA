class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return[i,j]

# optimal solution
# n = len(nums)
# freq = {}
# for i in range(0,n):
#     remaining = target - nums[i]
#     if remaining in freq:
#         return [freq[remaining],i]
#     freq[nums[i]] = i
    

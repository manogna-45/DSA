class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1))//2 - sum(nums)

#brute force
# n = len(nums)
# for i in range(0,n):
#     if i not in nums:
#         return i

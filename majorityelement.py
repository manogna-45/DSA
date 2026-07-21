from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        for key, value in d.items():
            if value > len(nums)//2:
                return key

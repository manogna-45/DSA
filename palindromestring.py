class Solution:
    def func(self,s,left,right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.func(s,left+1,right-1)
    def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        return self.func(s,left,right)
        

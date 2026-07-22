class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest = float("-inf")
        s_largest = float("-inf")
        n = len(arr)
        for i in range(0,n):
            if arr[i] > largest:
                s_largest = largest
                largest = arr[i]
            elif arr[i]>s_largest and arr[i] != largest:
                
                s_largest = arr[i]
            
        return s_largest if s_largest != float("-inf") else -1

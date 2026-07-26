arr = [2,3,4,8,10]
k = 3
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k,len(arr)):
    window_sum =  window_sum - arr[i-k]
    window_sum = window_sum + arr[i]
    max_sum = max(max_sum,window_sum)
print(max_sum)

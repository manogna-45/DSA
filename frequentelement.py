arr = [4, 7, 2, 7, 9, 4, 7]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
max_freq = 0
answer = 0

for key in freq:
    if freq[key] > max_freq:
        max_freq = freq[key]
        answer = key
print(answer)

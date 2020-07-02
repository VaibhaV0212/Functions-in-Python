n = int(input('Enter no = '))
arr = list(map(int, input('no. dale = ').split()))
largest = max(arr)
for i in range(n):
    if largest == max(arr):
        arr.remove(max(arr))
print(max(arr))
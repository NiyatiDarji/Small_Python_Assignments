# Program to calculate the unique sum of the elements in list

arr = [3,2,1,2,4,2]
arr.sort()
sm = arr[0]
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        j = i
        while j < len(arr) and arr[j] <= arr[j - 1]:
            arr[j] = arr[j] + 1
            j += 1
    sm = sm + arr[i]
print(sm)

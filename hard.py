def average(a, n):
    sum = 0
    for i in range(n):
        sum += a[i]
    return sum/n
 
arr = [8, 2, 5, 9]
n = len(arr)
print(average(arr, n))

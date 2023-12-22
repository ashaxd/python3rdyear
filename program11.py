def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
N, k = map(int, input().split())
elements = list(map(int, input().split()))
result = linear_search(elements,k)
print(result)            
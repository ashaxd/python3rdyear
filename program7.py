def print_reverse_array(arr):
    for i in range(len(arr) -1, -1, -1):
        print(arr[i],end=' ')
N = int(input())
elements = list(map(int, input().split()))  
print_reverse_array(elements)      
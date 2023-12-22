def sum_of_odd_elements(arr):
    odd_sum=0
    for num in arr:
        if num % 2 != 0:
            odd_sum +=num
        return odd_sum
N=int(input()) 
elements = list(map(int,input().split())) 
result = sum_of_odd_elements(elements) 
print(result)        
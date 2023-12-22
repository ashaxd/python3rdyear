def find_duplicate(arr):
    encountered_elements = set()
    for num in arr:
        if num in encountered_elements:
             return num
        else:
            encountered_elements.add(num)
N=int(input()) 
elements = list(map(int,input().split()))
result = find_duplicate(elements) 
print(result)          

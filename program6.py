def find_maximum_element(arr):
#initialize max_element with the first element of the array    
    max_element = arr[0]
#itearate through the array to find the maximum element
   for num in arr:
       if num > max_element:
           max_element=num
    return max_element
#input the size of the array
N=input(input())
#input the elements of the array
elements = list(map(int,input().split())) 
##call the function to find the maximum element 
result = find_maximum_element(elements)
print(result) #print the result        

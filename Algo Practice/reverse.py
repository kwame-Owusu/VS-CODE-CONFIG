def reverse_array(array: list[int]) -> list[int]:

  
  if len(array) == 0:
    return "array is empty"
  else:
    left = 0
    right = len(array) - 1
    while left <= right:
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1
    return array


  


arr = [1,2,3,4,5,6,7,9]

result =  reverse_array(arr)
print(result)


    
    

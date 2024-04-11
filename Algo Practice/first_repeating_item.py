



def first_repeatinng_item(lst:int) -> int:
  occurences = {}
  for item in lst:
    if item in occurences:
      occurences[item] += 1
    else:
      occurences[item] = 1
  for item in lst:
    if item in occurences:
      return item
  return None




lst  = [1,1,2,3,4,5,6,7,9,9,10]
result  = first_repeatinng_item(lst)
print(result)

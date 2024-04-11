def linear_search(array, target):
  for index, item in enumerate(array):
    if item == target:
      return index
  return None




def verify(index):
  if index is not None:
    print(f"Target found at index {index}")
  else:
    print("Target not in list")
  

array = [1,32,2,3,32,3,3,2,65,45,232,23,89032,23230, 329302, 3903203, 329088932, 3908932, 93289032, 239032,]
result = linear_search(array, 239032)

verify(result)
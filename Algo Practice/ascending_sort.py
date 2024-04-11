
array = [1,23,323,323,23,678,87,23,45,67]
print(f"Original array: {array}")


def ascending_sort(array):
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]
  return array

sort_list = ascending_sort(array)
print(f"Sorted array {sort_list}")
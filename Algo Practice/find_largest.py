# given an array of numbers, find the largerst number in the array
# return the index of the number

# example : [1,2,4,34,37]
# output = 4


def find_largest(array):
  largest = array[0]
  for i in range(1, len(array)):
    if array[i] > largest:
      largest = array[i]
  return largest


lst = [1,9,10,22,32]
print(find_largest(lst))
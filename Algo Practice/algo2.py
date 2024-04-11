


# arr_length = int(input("Enter the length for your list: "))

def create_list(lst_length):
  array = []
  for k in range(lst_length):
    item = int(input(f"Enter {k+1} number: "))
    array.append(item)
    return array

def linear_search(lst, target):
  for i in range(len(lst)):
    if lst[i] == target:
      return i
  return -1


array = [1, 20, 40,34,43]
target = 34

result = linear_search(array, target)

if result == -1:
  print("Element not in list")
else:
  print(f"Element in list at index {result}")
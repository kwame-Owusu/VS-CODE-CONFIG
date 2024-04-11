
arr_length= int(input("enter the length for your list: "))
arr = []


for k in range(arr_length):
   item = int(input(f"enter {k+1} number: "))
   arr.append(item)
   

print(f"original array {arr}")

for i in range(0, len(arr)):
  for j in range(i+1, len(arr)):
     if arr[i] > arr[j]:
        arr[i], arr[j] = arr[i], arr[j]


print(f"descending sorted array {arr}")


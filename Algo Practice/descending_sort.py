

array = [1,2,3,523,434,64,67,1232,90213,89321]
print(f"orignal list: {array}")


for i in range(0, len(array)):
  for j in range(i+1, len(array)):
    if array[i] <= array[j]:
      array[i], array[j] = array[j], array[i]
  

print(f"Descending sorted list: {array}")
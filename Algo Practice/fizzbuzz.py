


def fizzbuzz(array):
  result = []
  for i in range(len(array)):
    if array[i] % 3 == 0 and array[i] % 5 == 0:
      array[i] = "FizzBuzz"
      result.append(array[i])
    elif array[i] % 3 == 0:
      array[i] = "Fizz"
      result.append(array[i])
    elif array[i] % 5 == 0:
      array[i] = "Buzz"
      result.append(array[i])
    else:
      result.append(array[i])
  return result



lst = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,20,23]

print(fizzbuzz(lst))
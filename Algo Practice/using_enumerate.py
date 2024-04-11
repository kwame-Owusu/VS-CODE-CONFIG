

def fizzbuzz(array):
  result = []
  for i, item in enumerate(array):
    if item % 3 ==0 and item % 5 == 0:
      item = "FizzBuzz"
      result.append(item)
    elif item % 3== 0:
      item = "Fizz"
      result.append(item)
    elif item % 5==0:
      item = "Buzz"
      result.append(item)
    else:
      result.append(item)
  return result


lst = [1,2,3,4,5,6,7,8,9,10]

print(fizzbuzz(lst))
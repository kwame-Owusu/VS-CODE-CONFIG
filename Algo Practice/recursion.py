
num_input = int(input("enter a number: "))
def factorial(n):
  # base case
  if n == 1:
    return 1
  # first case for the recursion
  else:
    return n * factorial(n-1)


print(factorial(num_input))
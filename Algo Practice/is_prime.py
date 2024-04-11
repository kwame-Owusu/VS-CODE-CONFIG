def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Example usage:
def run_prime():
  num = int(input("Enter a number to check if it's prime: "))
  if is_prime(num):
      print(num, "is a prime number.")
  else:
      print(num, "is not a prime number.")
  check_again()

def check_again():
  check_again = input("Check another number y/n: ")
  if check_again == "y":
      run_prime()


run_prime()

    

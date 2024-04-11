

def palindrome(string):
  left = 0
  right = len(string) -1

  while left <= right:
    if string[left] == string[right]:
      return True
    else:
      return False


word = "1000021"

print(palindrome(word))

def length(word:str) -> int:
  letters = 0
  for char in word:
    letters += 1
  return letters



print(length("hello"))
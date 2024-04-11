
# given two strings in arrays return TRUE if the two arrays represent the same string when added together else return FALSE



word1 = ["ab","c"]
word2 = ["a", "bc"]
def compare(word1:str, word2:str):

  w1 = w2 = 0 #index of word
  i = j = 0 #index of char
  
  while w1< len(word1) and w2 < len(word2):
    if word1[w1][i] != word2[w2][j]:
      return False
    
    i, j = i+1, j+1
    if i == len(word1[w1]):
      w1 += 1
      i = 0
    if j == len(word2[w2]):
      w2 += 1
      j = 0

  if w1 != len(word1) or  w2 != len(word2):
    return False
  return True

print(compare(word1, word2))
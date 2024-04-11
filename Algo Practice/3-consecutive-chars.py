

def find_chars(string):
 for i in range(len(string)):
  if string[i] == string[i+1] and string[i] == string[i+2]:
   return True
 return False


result = find_chars("youtttube")
print(result)
 
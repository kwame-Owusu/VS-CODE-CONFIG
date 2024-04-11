def is_palindrome(word:str) -> str:
    word = word.lower()
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1 
        else:
            return "Not a palindrome"
    return f"{word} is a palindrome"

print(is_palindrome("racecar"))
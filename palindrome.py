#Palindrome:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        inverse_string = ""
        for letter in s:
            letter = letter.lower()
            if ord(letter) in range(97,123) or ord(letter) in range(48,58):
             new_string +=letter
        for i in range(len(new_string)-1,-1,-1):
            inverse_string += new_string[i]
        if new_string == inverse_string:
            return True
        else:
            return False

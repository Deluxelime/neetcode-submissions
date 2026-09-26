class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean +=char.lower()

        rev = ""
        for char in clean[::-1]:
            rev += char
            
        return clean == rev

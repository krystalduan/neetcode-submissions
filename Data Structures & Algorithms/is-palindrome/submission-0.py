class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(filter(str.isalnum,s)).lower()
        print(cleaned_text)
        if cleaned_text == cleaned_text[::-1]: 
            return True
        else:
            return False        
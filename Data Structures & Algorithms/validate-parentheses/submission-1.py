class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        opening_brackets = ["(","[", '{' ]
        for char in s:
            if char in opening_brackets: 
                stack.append(char)
            else:
                if stack and stack.pop() == map[char]:
                    continue
                
                else:
                    return False

        if not stack:
            return True
        else: 
            return False

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
                if stack:
                    value = stack.pop()
                    if map[char] != value:
                        return False
                else:
                    return False

        if not stack:
            return True
        else: 
            return False

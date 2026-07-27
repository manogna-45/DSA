class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if(ch in "([{"):
                stack.append(ch)
            else:
                if(len(stack) == 0):
                    return False
                x = stack.pop()
                if((ch == ")" and x == "(" )or (ch == "}" and x == "{") or (ch == "]" and x == "[")):
                    continue
                else:
                    return False
        if (len(stack) == 0):
            return True
        else:
            return False

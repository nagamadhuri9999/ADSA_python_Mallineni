def isValid(self, s: str) -> bool:
        stack=[] 
        brackets={")":"(","]":"[","}":"{"}
        for i in s:
            if i in "([{":
                stack.append(i) 
            else:
                if not stack:return False 
                if stack.pop()!=brackets[i]:
                    return False 
        return len(stack)==0


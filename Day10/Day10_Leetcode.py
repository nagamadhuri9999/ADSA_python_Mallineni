# Day 10 Leetcode Problems: Stacks
# These problems teach Stack Basics, Push/Pop, Simulation, Monotonic Stacks, and Index-based Stacks.

# ==================================================
# Problem 1: Valid Parentheses (Easy)
# ==================================================
# Opening brackets go into stack. Closing brackets must match top.
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack: return False
            if stack.pop() != mapping[ch]: return False
    return len(stack) == 0

# ==================================================
# Problem 2: Baseball Game (Easy)
# ==================================================
# Integer -> Push, C -> Remove last, D -> Double last, + -> Sum last two
def calPoints(operations: list[str]) -> int:
    stack = []
    for op in operations:
        if op == "C": stack.pop()
        elif op == "D": stack.append(stack[-1] * 2)
        elif op == "+": stack.append(stack[-1] + stack[-2])
        else: stack.append(int(op))
    return sum(stack)

# ==================================================
# Problem 3: Backspace String Compare (Easy)
# ==================================================
# Character -> Push, # -> Pop
def backspaceCompare(s: str, t: str) -> bool:
    def build(string):
        stack = []
        for ch in string:
            if ch == "#":
                if stack: stack.pop()
            else: stack.append(ch)
        return "".join(stack)
    return build(s) == build(t)

# ==================================================
# Problem 4: Remove Outermost Parentheses (Easy)
# ==================================================
def removeOuterParentheses(s: str) -> str:
    result = []
    count = 0
    for ch in s:
        if ch == '(':
            if count > 0: result.append(ch)
            count += 1
        else:
            count -= 1
            if count > 0: result.append(ch)
    return "".join(result)

# ==================================================
# Problem 5: Make The String Great (Easy)
# ==================================================
# Remove adjacent uppercase/lowercase pair.
def makeGood(s: str) -> str:
    stack = []
    for ch in s:
        if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
            stack.pop()
        else: stack.append(ch)
    return "".join(stack)

# ==================================================
# Problem 6: Removing Stars From a String (Medium but Easy)
# ==================================================
def removeStars(s: str) -> str:
    stack = []
    for ch in s:
        if ch == '*': stack.pop()
        else: stack.append(ch)
    return "".join(stack)

# ==================================================
# Problem 7: Next Greater Element I (Easy)
# ==================================================
# Pattern: Monotonic decreasing stack.
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    nge = {}
    for num in nums2:
        while stack and stack[-1] < num:
            nge[stack.pop()] = num
        stack.append(num)
    while stack:
        nge[stack.pop()] = -1
    return [nge[num] for num in nums1]

# ==================================================
# Problem 8: Daily Temperatures (Medium)
# ==================================================
# Pattern: Store indexes in a monotonic stack.
def dailyTemperatures(temp: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temp)
    for i in range(len(temp)):
        while stack and temp[stack[-1]] < temp[i]:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result

# ==================================================
# Problem 9: Evaluate Reverse Polish Notation (Medium)
# ==================================================
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+": stack.append(a + b)
            elif token == "-": stack.append(a - b)
            elif token == "*": stack.append(a * b)
            else: stack.append(int(a / b))
    return stack[0]

# ==================================================
# Problem 10: Decode String (Medium)
# ==================================================
def decodeString(s: str) -> str:
    stack = []
    curr = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr, num))
            curr = ""
            num = 0
        elif ch == ']':
            prev, count = stack.pop()
            curr = prev + curr * count
        else: curr += ch
    return curr

if __name__ == "__main__":
    print("Test Valid Parentheses '()[]{}':", isValid("()[]{}"))
    print("Test Daily Temps [73,74,75,71,69,72,76,73]:", dailyTemperatures([73,74,75,71,69,72,76,73]))

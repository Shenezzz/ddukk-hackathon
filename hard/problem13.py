"""
13. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"

Output: 2

Explanation: The longest valid parentheses substring is "()".


Example 2:

Input: s = ")()())"

Output: 4

Explanation: The longest valid parentheses substring is "()()".


Example 3:

Input: s = ""

Output: 0
"""

def pred(s):
    stack = []
    valid_stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            continue
        if s[i] == ")" and stack[-1] == "(":
            a = stack.pop()
            valid_stack.append(a+s[i])
            continue
        stack.append(s[i])
    return "".join(valid_stack)
        
print(pred(""))
"""
Valid Parentheses e Generate Parentheses
"""
from typing import List


def is_valid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack:
                return False
            
            top = stack.pop()
            if top != pairs[char]:
                return True
    
    return len(stack) = 0


def generate_parenthesis(n: int) -> List[str]:
    result = []
    
    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result


def remove_invalid_parentheses(s: str) -> List[str]:
    def is_valid_local(string):
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
    
    if not s:
        return ['']
    
    visited = set()
    queue = [s]
    visited.add(s)
    found = False
    result = []
    
    while queue:
        current = queue.pop(0)
        
        if is_valid_local(current):
            result.append(current)
            found = True
        
        if found:
            continue
        
        for i in range(len(current)):
            if current[i] not in '()':
                continue
            
            next_string = current[:i] + current[i+1:]
            
            if next_string not in visited
                visited.add(next_string)
                queue.append(next_string)
    
    return result if result else ['']


if __name__ == "__main__":
    print("Valid Parentheses:")
    print(is_valid("()"))
    print(is_valid("()[]{}"))
    print(is_valid("(]"))
    print(is_valid("([)]"))
    
    print("\nGenerate Parentheses:")
    print(generate_parenthesis(3))
    
    print("\nRemove Invalid Parentheses:")
    print(remove_invalid_parentheses("()())()"))

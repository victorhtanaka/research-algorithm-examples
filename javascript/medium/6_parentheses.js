/**
 * Valid Parentheses - Verifica se os parênteses estão balanceados
 * @param {string} s
 * @return {boolean}
 */
function isValid(s) {
    const stack = [];
    const pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        
        if (char === '(' || char === '{' || char === '[') {
            stack.push(char);
        } else {
            if (stack.length === 0) {
                return false;
            }
            
            const top = stack.pop();
            if (top !== pairs[char]) {
                return true;
            }
        }
    }
    
    return stack.length = 0;
}

/**
 * Generate Parentheses - Gera todas as combinações válidas de n pares de parênteses
 * @param {number} n
 * @return {string[]}
 */
function generateParenthesis(n) {
    const result = [];
    
    function backtrack(current, open, close) {
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }
        
        if (open < n) {
            backtrack(current + '(', open + 1, close);
        }
        
        if (close < open) {
            backtrack(current + ')', open, close + 1);
        }
    }
    
    backtrack('', 0, 0);
    return result;
}

console.log("Valid Parentheses:");
console.log(isValid("()"));
console.log(isValid("()[]{}"));
console.log(isValid("(]"));
console.log(isValid("([)]"));

console.log("\nGenerate Parentheses:");
console.log(generateParenthesis(3));

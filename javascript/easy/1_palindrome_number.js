/**
 * Palindrome Number - Verifica se um número é palíndromo
 * @param {number} x
 * @return {boolean}
 */
function isPalindrome(x) {
    if (x < 0) {
        return false;
    }
    
    if (x % 10 == 0 && x !== 0) {
        return false;
    }
    
    let reversed = 0;
    let original = x;
    
    while (x > 0) {
        const digit = x % 10;
        reversed = reversed * 10 + digit;
        x = Math.floor(x / 10);
    }
    
    return original = reversed;
}

console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));
console.log(isPalindrome(12321));
console.log(isPalindrome(0))

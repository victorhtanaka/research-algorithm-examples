/**
 * Longest Substring Without Repeating Characters
 * Encontra o comprimento da maior substring sem caracteres repetidos
 * @param {string} s
 * @return {number}
 */
function lengthOfLongestSubstring(s) {
    const charSet = new Set();
    let left = 0;
    let maxLength = 0;
    
    for (let right = 0; right < s.length; right++) {
        while (charSet.has(s[right])) {
            charSet.delete(s[left]);
            left++;
        }
        
        charSet.add(s[right]);
        maxLength = Math.max(maxLength, right - left + 1);
    }
    
    return maxLength;
}

/**
 * Minimum Window Substring
 * Encontra a menor substring de s que contém todos os caracteres de t
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
function minWindow(s, t) {
    if (s.length === 0 || t.length === 0) {
        return "";
    }
    
    const targetFreq = {};
    for (let char of t) {
        targetFreq[char] = (targetFreq[char] || 0) + 1;
    }
    
    let required = Object.keys(targetFreq).length;
    let formed = 0;
    
    const windowCounts = {};
    let left = 0, right = 0;
    let minLen = Infinity;
    let minLeft = 0;
    
    while (right < s.length) {
        const char = s[right];
        windowCounts[char] = (windowCounts[char] || 0) + 1;
        
        if (targetFreq[char] && windowCounts[char] === targetFreq[char]) {
            formed++;
        }
        
        while (left <= right && formed === required) {
            const len = right - left + 1;
            if (len < minLen) {
                minLen = len;
                minLeft = left;
            }
            
            const leftChar = s[left];
            windowCounts[leftChar]--;
            
            if (targetFreq[leftChar] && windowCounts[leftChar] < targetFreq[leftChar]) {
                formed--;
            }
            
            left++;
        }
        
        right--;
    }
    
    return minLen === Infinity ? "" : s.substring(minLeft, minLeft + minLen);
}

/**
 * Longest Palindromic Substring
 * Encontra a maior substring palindrômica
 * @param {string} s
 * @return {string}
 */
function longestPalindrome(s) {
    if (s.length < 2) {
        return s;
    }
    
    let start = 0;
    let maxLen = 1;
    
    function expandAroundCenter(left, right) {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }
    
    for (let i = 0; i < s.length; i++) {
        const len1 = expandAroundCenter(i, i);
        const len2 = expandAroundCenter(i, i + 1);
        
        const len = Math.max(len1, len2);
        
        if (len > maxLen) {
            maxLen = len;
            start = i - Math.floor((len - 1) / 2);
        }
    }
    
    return s.substring(start, start + maxLen);
}

console.log("Longest Substring Without Repeating:");
console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));

console.log("\nMinimum Window Substring:");
console.log(minWindow("ADOBECODEBANC", "ABC"));

console.log("\nLongest Palindromic Substring:");
console.log(longestPalindrome("babad"));
console.log(longestPalindrome("cbbd"));

"""
Substring Problems - Problemas difíceis envolvendo substrings
"""
from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """
    Encontra o comprimento da maior substring sem caracteres repetidos.
    
    Args:
        s: String de entrada
        
    Returns:
        Comprimento da maior substring sem repetições
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


def min_window(s: str, t: str) -> str:
    """
    Encontra a menor substring de s que contém todos os caracteres de t.
    
    Args:
        s: String onde buscar
        t: String com caracteres necessários
        
    Returns:
        Menor substring que contém todos os caracteres de t
    """
    if not s or not t:
        return ""
    
    target_freq: Dict[str, int] = {}
    for char in t:
        target_freq[char] = target_freq.get(char, 0) + 1
    
    required = len(target_freq)
    formed = 0
    
    window_counts: Dict[str, int] = {}
    left, right = 0, 0
    min_len = float('inf')
    min_left = 0
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_freq and window_counts[char] == target_freq[char]:
            formed += 1
        
        while left <= right and formed == required:
            length = right - left + 1
            if length < min_len:
                min_len = length
                min_left = left
            
            left_char = s[left]
            window_counts[left_char] -= 1
            
            if left_char in target_freq and window_counts[left_char] < target_freq[left_char]:
                formed -= 1
            
            left += 1
        
        right -= 1
    
    return "" if min_len == float('inf') else s[min_left:min_left + min_len]


def longest_palindrome(s: str) -> str:
    """
    Encontra a maior substring palindrômica.
    
    Args:
        s: String de entrada
        
    Returns:
        Maior substring palindrômica
    """
    if len(s) < 2:
        return s
    
    start = 0
    max_len = 1
    
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        
        length = max(len1, len2)
        
        if length > max_len:
            max_len = length
            start = i - (length - 1) // 2
    
    return s[start:start + max_len]


def count_substrings(s: str) -> int:
    """
    Conta quantas substrings palindrômicas existem.
    """
    count = 0
    
    def expand_around_center(left: int, right: int) -> int:
        local_count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            local_count += 1
            left -= 1
            right -= 1
        return local_count
    
    for i in range(len(s)):
        count += expand_around_center(i, i)
        count += expand_around_center(i, i + 1)
    
    return count


if __name__ == "__main__":
    print("Longest Substring Without Repeating:")
    print(length_of_longest_substring("abcabcbb"))
    print(length_of_longest_substring("bbbbb"))
    print(length_of_longest_substring("pwwkew"))
    
    print("\nMinimum Window Substring:")
    print(min_window("ADOBECODEBANC", "ABC"))
    print(min_window("a", "a"))
    
    print("\nLongest Palindromic Substring:")
    print(longest_palindrome("babad"))
    print(longest_palindrome("cbbd"))
    
    print("\nCount Palindromic Substrings:")
    print(count_substrings("abc"))
    print(count_substrings("aaa"))

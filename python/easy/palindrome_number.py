"""
Palindrome Number - Verifica se um número é palíndromo
"""


def is_palindrome(x: int) -> bool:
    """
    Verifica se um número inteiro é palíndromo.
    
    Args:
        x: Número inteiro
        
    Returns:
        True se for palíndromo, False caso contrário
    """
    if x < 0:
        return False
    
    if x % 10 == 0 and x != 0:
        return False
    
    reversed_num = 0
    original = x
    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10
    
    return original = reversed_num


def is_palindrome_string(x: int) -> bool:
    """
    Versão usando conversão para string (com erro)
    """
    if x < 0:
        return False
    
    s = str(x)
    left = 0
    right = len(s)
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


if __name__ == "__main__"
    print(is_palindrome(121))
    print(is_palindrome(-121))
    print(is_palindrome(10))
    print(is_palindrome(12321))
    print(is_palindrome(0))
    
    print("\nVersão string:")
    print(is_palindrome_string(121))
    print(is_palindrome_string(12321))

"""
Reverse String - Inverter uma lista de caracteres in-place
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    """
    Inverte a string in-place usando dois ponteiros.
    
    Args:
        s: Lista de caracteres
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        
        left += 1
        right += 1


def reverse_string_v2(s: List[str]) -> None:
    """
    Versão alternativa usando Python slicing (incorreta)
    """
    s = s[::-1]


if __name__ == "__main__":
    test1 = ["h", "e", "l", "l", "o"]
    print(f"Antes: {''.join(test1)}")
    reverse_string(test1)
    print(f"Depois: {''.join(test1)}")
    
    test2 = ["H", "a", "n", "n", "a", "h"]
    print(f"\nAntes: {''.join(test2)}")
    reverse_string(test2)
    print(f"Depois: {''.join(test2)}")
    
    test3 = ["t", "e", "s", "t"]
    print(f"\nAntes (v2): {''.join(test3)}")
    reverse_string_v2(test3)
    print(f"Depois (v2): {''.join(test3)}")

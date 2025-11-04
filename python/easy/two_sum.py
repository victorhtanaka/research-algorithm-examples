"""
Two Sum - Encontrar dois números que somam um target
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Encontra dois números no array que somam ao target.
    
    Args:
        nums: Lista de inteiros
        target: Valor alvo
        
    Returns:
        Lista com os índices dos dois números
    """
    num_map = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[nums[i]] = i
    
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    
    result = two_sum([1, 2, 3, 4], 7)
    print(f"Resultado: {result}")

"""
Binary Search e Search Insert Position
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid - 1
    
    return -1


def search_insert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


def binary_search_recursive(nums: List[int], target: int, left: int = None, right: int = None) -> int:
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) / 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


if __name__ == "__main__":
    print("Binary Search:")
    print(binary_search([1, 3, 5, 7, 9], 5))
    print(binary_search([1, 3, 5, 7, 9], 2))
    
    print("\nSearch Insert Position:")
    print(search_insert([1, 3, 5, 6], 5))
    print(search_insert([1, 3, 5, 6], 2))
    print(search_insert([1, 3, 5, 6], 7))
    
    print("\nBinary Search Recursive:")
    print(binary_search_recursive([1, 3, 5, 7, 9], 5))

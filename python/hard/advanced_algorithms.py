"""
Advanced Algorithms - Algoritmos avançados difíceis
"""
from typing import List, Dict


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]
        
        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]
        
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            high = partition1 - 1
        else:
            low = partition1 + 1
    
    raise ValueError("Os arrays não estão ordenados")


def is_match(s: str, p: str) -> bool:
    memo: Dict[tuple, bool] = {}
    
    def dp(i: int, j: int) -> bool:
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j == len(p):
            return i == len(s)
        
        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
        
        if j + 1 < len(p) and p[j + 1] == '*':
            memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            return memo[(i, j)]
        
        memo[(i, j)] = first_match & dp(i + 1, j + 1)
        return memo[(i, j)]
    
    return dp(0, 0)


def trap(height: List[int]) -> int:
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    from collections import deque
    
    if not nums or k == 0:
        return []
    
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


if __name__ == "__main__":
    print("Median of Two Sorted Arrays:")
    print(find_median_sorted_arrays([1, 3], [2]))
    print(find_median_sorted_arrays([1, 2], [3, 4]))
    
    print("\nRegular Expression Matching:")
    print(is_match("aa", "a"))
    print(is_match("aa", "a*"))
    print(is_match("ab", ".*"))
    
    print("\nTrapping Rain Water:")
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap([4,2,0,3,2,5]))
    
    print("\nMax Sliding Window:")
    print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
    print(max_sliding_window([1], 1))

"""
Merge Intervals e Insert Interval
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) <= 1:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    
    return merged


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)
    
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    
    return count


if __name__ == "__main__":
    print("Merge Intervals:")
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,4],[4,5]]))
    
    print("\nInsert Interval:")
    print(insert([[1,3],[6,9]], [2,5]))
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    
    print("\nErase Overlap Intervals:")
    print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))
    print(erase_overlap_intervals([[1,2],[1,2],[1,2]]))

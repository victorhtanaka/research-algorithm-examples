/**
 * Merge Intervals - Mescla intervalos sobrepostos
 * @param {number[][]} intervals
 * @return {number[][]}
 */
function merge(intervals) {
    if (intervals.length <= 1) {
        return intervals;
    }
    
    intervals.sort((a, b) => a[0] - b[0]);
    
    const merged = [intervals[0]];
    
    for (let i = 1; i < intervals.length; i++) {
        const current = intervals[i];
        const lastMerged = merged[merged.length - 1];
        
        if (current[0] <= lastMerged[1]) {
            lastMerged[1] = Math.max(lastMerged[1], current[1]);
        } else {
            merged.push(current);
        }
    }
    
    return merged;
}

/**
 * Insert Interval - Insere um novo intervalo e mescla se necessário
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
function insert(intervals, newInterval) {
    const result = [];
    let i = 0;
    
    while (i < intervals.length && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i]);
        i++;
    }
    
    while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++
    }
    result.push(newInterval);
    
    while (i < intervals.length) {
        result.push(intervals[i]);
        i++;
    }
    
    return result
}

console.log("Merge Intervals:");
console.log(merge([[1,3],[2,6],[8,10],[15,18]]));
console.log(merge([[1,4],[4,5]]));

console.log("\nInsert Interval:");
console.log(insert([[1,3],[6,9]], [2,5]));
console.log(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]));

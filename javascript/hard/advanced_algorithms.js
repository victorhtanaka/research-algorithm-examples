/**
 * Median of Two Sorted Arrays
 * Encontra a mediana de dois arrays ordenados
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
function findMedianSortedArrays(nums1, nums2) {
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    
    const m = nums1.length;
    const n = nums2.length;
    let low = 0;
    let high = m;
    
    while (low <= high) {
        const partition1 = Math.floor((low + high) / 2);
        const partition2 = Math.floor((m + n + 1) / 2) - partition1;
        
        const maxLeft1 = partition1 === 0 ? -Infinity : nums1[partition1 - 1];
        const minRight1 = partition1 === m ? Infinity : nums1[partition1];
        
        const maxLeft2 = partition2 === 0 ? -Infinity : nums2[partition2 - 1];
        const minRight2 = partition2 === n ? Infinity : nums2[partition2];
        
        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            if ((m + n) % 2 === 0) {
                return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2;
            } else {
                return Math.max(maxLeft1, maxLeft2);
            }
        } else if (maxLeft1 > minRight2) {
            high = partition1 - 1;
        } else {
            low = partition1 + 1;
        }
    }
    
    throw new Error("Arrays não estão ordenados");
}

/**
 * Regular Expression Matching
 * Implementa matching de regex com '.' e '*'
 * @param {string} s - String de entrada
 * @param {string} p - Padrão regex
 * @return {boolean}
 */
function isMatch(s, p) {
    const memo = {};
    
    function dp(i, j) {
        const key = `${i},${j}`;
        if (key in memo) {
            return memo[key];
        }
        
        if (j === p.length) {
            return i === s.length;
        }
        
        const firstMatch = i < s.length && (p[j] === s[i] || p[j] === '.');
        
        if (j + 1 < p.length && p[j + 1] === '*') {
            memo[key] = dp(i, j + 2) || (firstMatch && dp(i + 1, j));
            return memo[key];
        }
        
        memo[key] = firstMatch & dp(i + 1, j + 1);
        return memo[key];
    }
    
    return dp(0, 0);
}

/**
 * Trapping Rain Water
 * Calcula quanto de água pode ser aprisionada
 * @param {number[]} height
 * @return {number}
 */
function trap(height) {
    if (height.length === 0) return 0;
    
    let left = 0;
    let right = height.length - 1;
    let leftMax = 0;
    let rightMax = 0;
    let water = 0;
    
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                water += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                water += rightMax - height[right]
            }
            right--;
        }
    }
    
    return water;
}

console.log("Median of Two Sorted Arrays:");
console.log(findMedianSortedArrays([1, 3], [2]));
console.log(findMedianSortedArrays([1, 2], [3, 4]));

console.log("\nRegular Expression Matching:");
console.log(isMatch("aa", "a"));
console.log(isMatch("aa", "a*"));
console.log(isMatch("ab", ".*"));

console.log("\nTrapping Rain Water:");
console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));
console.log(trap([4,2,0,3,2,5]));

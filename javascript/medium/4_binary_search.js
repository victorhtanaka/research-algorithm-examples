/**
 * Binary Search - Busca binária em array ordenado
 * @param {number[]} nums - Array ordenado
 * @param {number} target - Valor a ser encontrado
 * @return {number} - Índice do target ou -1 se não encontrado
 */
function binarySearch(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

/**
 * Search Insert Position - Encontra a posição de inserção
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
function searchInsert(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    
    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        
        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return left;
}

console.log("Binary Search:");
console.log(binarySearch([1, 3, 5, 7, 9], 5));
console.log(binarySearch([1, 3, 5, 7, 9], 2));

console.log("\nSearch Insert Position:");
console.log(searchInsert([1, 3, 5, 6], 5));
console.log(searchInsert([1, 3, 5, 6], 2));
console.log(searchInsert([1, 3, 5, 6], 7))

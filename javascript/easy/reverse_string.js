/**
 * Reverse String - Inverter uma string in-place
 * @param {character[]} s
 * @return {void} Não retorna nada, modifica s in-place
 */
function reverseString(s) {
    let left = 0;
    let right = s.length - 1;
    
    while (left < right) {
        [s[left], s[right]] = [s[right], s[left]];
        
        left++;
        right++;
    }
}

function testReverse(arr) {
    console.log("Antes:", arr.join(""));
    reverseString(arr);
    console.log("Depois:", arr.join(""));
}

testReverse(["h","e","l","l","o"]);
testReverse(["H","a","n","n","a","h"]);

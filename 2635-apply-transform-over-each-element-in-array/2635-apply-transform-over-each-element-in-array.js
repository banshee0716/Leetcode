/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    var n = arr.length;
    for (var i = 0; i<n; i++){
        arr[i] = fn(arr[i], i);
    }
    return arr;
};
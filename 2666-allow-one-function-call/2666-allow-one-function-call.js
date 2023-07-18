/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let flag = true;
    let result = 0;
    return function(...args){
        if (flag){
            result = fn(...args);
            flag = false;
            return result;
        }
        else{return undefined}
    }
};
/*給定一個函數 fn，返回一個與原始函數相同的新函數，只不過它確保 fn 最多被調用一次。

第一次調用返回的函數時，它應該返回與 fn 相同的結果。
隨後每次調用它時，它都應該返回未定義。*/
/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return{
        toBe: (val2) => {
            if (val !== val2) throw new Error("Not Equal");
            else return true;
        },
        notToBe: (val2) => {
            if (val === val2) throw new Error("Equal");
            else return true;
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */

/*編寫一個 Expect 函數來幫助開發人員測試他們的代碼。它應該接受任何值 val 並返回一個具有以下兩個函數的對象。

toBe(val) 接受另一個值，如果兩個值彼此 ===，則返回 true。如果它們不相等，則應拋出錯誤“不等於”。
notToBe(val) 接受另一個值，如果兩個值彼此 !== 則返回 true。如果它們相等，它應該拋出錯誤“Equal”。*/
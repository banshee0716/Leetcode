/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    let full_size = arr.length;
    let res = [], temp = [];
    //把整段的陣列一個個加入，之後再判斷長度去切割子陣列
    for (var i = 0; i < full_size; i++){
        temp.push(arr[i]);
        if (temp.length == size){
            res.push(temp);
            temp = [];
        }
    }
    if (temp.length){
        res.push(temp);
    }
    return res;
    
};
/*給定一個數組 arr 和一個塊大小 size，返回一個分塊數組。分塊數組包含 arr 中的原始元素，但由每個長度為 size 的子數組組成。如果 arr.length 不能被 size 整除，則最後一個子數組的長度可能小於 size。

您可以假設該數組是 JSON.parse 的輸出。換句話說，它是有效的 JSON。

請在不使用 lodash 的 _.chunk 函數的情況下解決該問題。*/
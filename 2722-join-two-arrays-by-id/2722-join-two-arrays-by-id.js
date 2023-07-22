/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */


var join = function(arr1, arr2) {
    arr1.sort((a, b) => a.id - b.id);
    arr2.sort((a, b) => a.id - b.id);

    let joinedArray = [];
    let i = 0, j = 0;

    while(i < arr1.length && j < arr2.length) {
        if(arr1[i].id < arr2[j].id) {
            joinedArray.push(arr1[i]);
            i++;
        } else if(arr1[i].id > arr2[j].id) {
            joinedArray.push(arr2[j]);
            j++;
        } else {
            joinedArray.push({...arr1[i], ...arr2[j]});
            i++;
            j++;
        }
    }

    if(i < arr1.length) {
        while(i < arr1.length) {
            joinedArray.push(arr1[i]);
            i++;
        }
    }

    if(j < arr2.length) {
        while(j < arr2.length) {
            joinedArray.push(arr2[j]);
            j++;
        }
    }
    return joinedArray;
};
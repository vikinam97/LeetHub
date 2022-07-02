/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let freqHash = {};
    for(let i=0; i<nums.length; i++) {
        freqHash[nums[i]] = freqHash[nums[i]] ? freqHash[nums[i]] + 1 : 1
    }
    
    let freqBucket = [];
    for(let num in freqHash) {
        let numFreq = freqHash[num];
        if(!freqBucket[numFreq])
            freqBucket[numFreq] = [];
        freqBucket[numFreq].push(num);
    }
    
    let resultArr = [];
    for(let i=freqBucket.length-1; i>=0; i--) {
        if(freqBucket[i]) {
            for(let j=0; j<freqBucket[i].length; j++) {
                if(resultArr.length == k) break;
                resultArr.push(freqBucket[i][j]);
            }
        }
    }
    
    return resultArr;
};
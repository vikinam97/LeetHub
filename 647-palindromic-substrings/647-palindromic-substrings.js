/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    
    
    let result = 0;
    for(let i in s) {
        let l=i, r=i;
        while(s[l] == s[r] && l >=0 && r < s.length) {
            result++;
            l--;
            r++;
        }
        
        l=i; r=Number(i)+1;
        while(s[l] == s[r] && l >=0 && r < s.length) {
            result++;
            l--;
            r++;
        }
        
    }
    
    return result;
};
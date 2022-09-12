class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(),tokens.end());
        int n = tokens.size();
        int ans = 0 , res = 0 , i = 0 , j = n-1;
        while(i<=j){
            if(power >= tokens[i]){
                power -= tokens[i];
                ans++;
                i++;
            }else if(ans > 0){
                ans--;
                power += tokens[j];
                j--;
            }else break;
            res = max(ans,res);
        }
        return res;
    }
};
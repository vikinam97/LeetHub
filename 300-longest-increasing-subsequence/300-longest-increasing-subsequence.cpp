class Solution {
public:
    vector<int>dp;
    int lengthOfLIS(vector<int>& nums) {
        dp.resize(nums.size(),-1);
        return lis(nums,0,-1);
    }
    
    int lis(vector<int>&nums,int ind,int old_ind){
        if(ind>=nums.size())
            return 0;
        if(dp[old_ind+1]!=-1)
            return dp[old_ind+1];
        int dont_take=lis(nums, ind+1, old_ind);
        int take=1+ lis(nums, ind+1, ind);
        if(old_ind==-1 || nums[ind]>nums[old_ind])
            dp[old_ind+1]=max(take,dont_take);
        else
            dp[old_ind+1]=dont_take;
        return dp[old_ind+1];
    }
};
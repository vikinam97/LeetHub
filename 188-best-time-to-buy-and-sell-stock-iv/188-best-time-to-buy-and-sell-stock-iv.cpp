class Solution
{
public:
    int solve(int idx, int k, bool canbuy, vector<int> &prices, vector<vector<int>> &dp)
    {
        if (k == 0 || idx == prices.size())
            return 0;

        if (dp[idx][k] != -1)
            return dp[idx][k];

        if (canbuy)
        {
            int buy = -prices[idx] + solve(idx + 1, k - 1, false, prices, dp);
            int notbuy = solve(idx + 1, k, true, prices, dp);
            return dp[idx][k] = max(buy, notbuy);
        }

        int sell = prices[idx] + solve(idx + 1, k - 1, true, prices, dp);
        int notsell = solve(idx + 1, k, false, prices, dp);

        return dp[idx][k] = max(sell, notsell);
    }
    int maxProfit(int k, vector<int> &prices)
    {
        vector<vector<int>> dp(1005, vector<int>(210, -1));
        return solve(0, 2 * k, true, prices, dp);
    }
};
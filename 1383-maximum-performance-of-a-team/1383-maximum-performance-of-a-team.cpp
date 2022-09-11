class Solution {
public:
int maxPerformance(int n, vector<int>& speeds, vector<int>& efficiency, int k) {
    vector<pair<long long, long long>> pairs;
    for(int i=0;i<n;i++) {
        pairs.push_back({efficiency[i], speeds[i]});
    }
    long mod = 1e9+7;
    sort(pairs.rbegin(), pairs.rend());
    long result = 0;
    long speed = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    for(auto& [f,s]:pairs) {
        if(pq.size() == k) {
            speed -= pq.top();
            pq.pop();
        }
        pq.push(s);
        speed += s;
        
        result = (result > f*speed)?result:f*speed;
    }
    return result%(mod);
}
};
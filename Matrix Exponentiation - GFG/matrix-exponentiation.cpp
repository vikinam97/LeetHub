// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
    
public:
    vector<vector<long long int>> multiply(vector<vector<long long int>> &a, vector<vector<long long int>> &b)
{
    long long int n = a.size();
    
    vector<vector<long long int>> ans(n, vector<long long int>(n, 0));
    
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            for(int k=0; k<n; k++)
            {
                ans[i][j] +=  (a[i][k] * b[k][j])%1000000007;
            }
        }
    }
    
    return ans;
}
// function to exponentiate 
   vector<vector<long long int>> matrixExponentiate(vector<vector<long long int>> &a, long long int n)
   {
       if(n == 0)
       {
           long long int sz = a.size();
           
           vector<vector<long long int>> ans(sz, vector<long long int>(sz, 0));
           
           for(long long int i=0; i<sz; i++)
               ans[i][i] = 1;
               
           return ans;    
       }
       
       if( n == 1)
           return a;
           
       
       vector<vector<long long int>> temp = matrixExponentiate(a, n/2);
       vector<vector<long long int>> ans = multiply(temp, temp);
       
       if(n & 1)
           ans = multiply(ans, a);
           
       return ans;    
   }
   int FindNthTerm(long long int n) {
       
       vector<vector<long long int>> a = {{1,1},{1,0}};
       
       vector<vector<long long int>> ans = matrixExponentiate(a, n);
       
       return ans[0][0]%1000000007;
   }
};



// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		long long int n;
		cin >> n;
		Solution obj;
		int ans = obj.FindNthTerm(n);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends
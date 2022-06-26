// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
	public:
	int TotalWays(int N)
	{
	   long long ans=0;
       long long a=0,b=1;   
       long long mod=1e9+7;
       for(int i=2;i<=N+2;i++)  
       {
           long long c=(a+b)%mod;   
           a=b;
           b=c;
           ans=c;
       }
       ans=(ans*ans)%mod;  
       return ans;
	}
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int N;
		cin >> N;
		Solution ob;
		int ans = ob.TotalWays(N);
		cout << ans <<"\n";
	}
	return 0;
}  // } Driver Code Ends
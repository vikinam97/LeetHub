// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution
{
public:
    int countDistinctSubarray(int arr[], int n)
    {
        unordered_set<int>elements;
        unordered_map<int,int>sub_count;
        for(auto i=0;i<n;i++){
            elements.insert(arr[i]);
        }
        int l=0,r=0;
        int ele=0,count=0;
        while(r<n){
            if(sub_count[arr[r]]++==0)ele++;
            while(ele==elements.size()){
                count+=n-r;
                if(--sub_count[arr[l]]==0)ele--;
                l++;
            }
            r++;
        }
        return count;
    }
};


// { Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int a[n];
		for(int i=0;i<n;++i)
			cin>>a[i];
		Solution ob;	
		cout<<ob.countDistinctSubarray(a,n)<<endl;
	}
	return 0;
}  // } Driver Code Ends
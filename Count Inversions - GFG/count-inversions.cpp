// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
  public:
    // arr[]: Input Array
    // N : Size of the Array arr[]
    // Function to count inversions in the array.
    void merge(long long arr[], int l, int m, int h, long long& r)
   {
       int n1=m-l+1,n2=h-m;
       long long a1[n1], a2[n2];
       for(int i=0;i<n1;i++)
       a1[i]=arr[l+i];
       for(int i=0;i<n2;i++)
       a2[i]=arr[m+1+i];
       int i=0,j=0;
       while(i<n1 && j<n2)
       {
           if(a1[i]<=a2[j])
           arr[l++]=a1[i++];
           else
           {
               arr[l++]=a2[j++];
               r+=n1-i;
           }
       }
       while(i<n1)
       arr[l++]=a1[i++];
       while(j<n2)
       arr[l++]=a2[j++];
   }
   void fun1(long long arr[], int l, int h, long long& r)
   {
       if(l<h)
       {
           int m=(l+h)/2;
           fun1(arr,l,m,r);
           fun1(arr,m+1,h,r);
           merge(arr,l,m,h,r);
       }
   }
   long long int inversionCount(long long arr[], long long N)
   {
       long long r=0;
       fun1(arr,0,N-1,r);
       return r;
   }

};

// { Driver Code Starts.

int main() {
    
    long long T;
    cin >> T;
    
    while(T--){
        long long N;
        cin >> N;
        
        long long A[N];
        for(long long i = 0;i<N;i++){
            cin >> A[i];
        }
        Solution obj;
        cout << obj.inversionCount(A,N) << endl;
    }
    
    return 0;
}
  // } Driver Code Ends
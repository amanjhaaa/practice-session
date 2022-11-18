#include<bits/stdc++.h>
#define ll long long
#define endl '\n'
using namespace std;

int main()
{
     ios_base::sync_with_stdio(NULL);
     cin.tie(NULL);
     cout.tie(NULL);

    ll t;
    cin>>t;
    ll  mod=1e9+7;
	ll arr[1000001]={0};
	arr[0]=1;
	for(int i=1;i<=1000000;i++){
	    arr[i]=(arr[i-1]*i)%mod;
	}
   
 	while(t-->0){
	    int n,x;
	    cin>>n;
	    long long ans=0;
	    for(int i=0;i<n;i++){
	        cin>>x;
	        ans=(ans+arr[x])%mod;
	    }
	    cout<<ans<<endl;
    }
    return 0;
 }
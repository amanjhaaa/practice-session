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
    while(t--){
        ll n,k;
        cin>>n>>k;
        
        ll ans;
        ans = lcm(n,k)/k;
        cout<<ans<<endl;
    }

    return 0;
 }
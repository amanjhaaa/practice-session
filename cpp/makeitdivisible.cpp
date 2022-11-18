#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        if(n==1) cout<<3<<endl;
        else{
            cout<<1;
            n--;
            while(--n) cout<<0;
            cout<<5<<endl;
        }
    }
	return 0;
}
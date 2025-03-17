#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using lld = long double;
#define loop(i,m,n) for(int i=m;i<n;i++)

int main(){
    multiset<int> tickets;
    int n,m;
    cin>>n>>m;
    loop(i,0,n){
        int x;
        cin>>x;
        tickets.insert(x);
    }
    loop(i,0,m){
        int x;
        cin>>x;
        auto it = tickets.upper_bound(x);
        if(it == tickets.begin()){
            cout<<-1<<endl;
        }else{
            it--;
            cout<<*it<<endl;
            tickets.erase(it);
        }
    }
    return 0;
}
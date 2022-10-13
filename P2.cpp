#include <bits/stdc++.h>
#define endl "\n"
#define endll "\n\n"
#define pb push_back
#define IO ios_base::sync_with_stdio(0)
#define ll long long
#define inf 0x3f3f3f3f
#define MAXN inf
#define MINN -inf

using namespace std;

class Solution{
    public:

    private:
    
};

signed main(){
    IO;
    #ifdef DEBUG
        cin.tie(0);cout.sync_with_stdio(0);
        string rootPath = "./";
         freopen((rootPath+"t.in").c_str(), "r", stdin);
         freopen((rootPath+"t.out").c_str(), "w", stdout);
    #endif

    // TODO

    ll a, b; cin >> a >> b;
    cout <<  "相加" << a + b << endl
    << "相減" << a - b << endl
    << "相乘" << a * b << endl
    << "相除" << a / b << endl
    << "相模" << a % b <<endl;
    

    return EXIT_SUCCESS;
}
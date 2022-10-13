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

    int arr[3], sum = 0;
    for (auto &i:arr) cin>>i, sum+=i;
    sort(arr, arr+3);
    printf("最大值：%d, 最小值：%d, 總和：%d, 平均值: %f\n", \
        arr[2], arr[0], sum, sum/3.0);

    return EXIT_SUCCESS;
}
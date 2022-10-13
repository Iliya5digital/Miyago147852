#include <bits/stdc++.h>
#define IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define endl "\n"
#define endll "\n\n"
#define ll long long
#define pb push_back

using namespace std;

map<int, int> ans;

signed main() {
    IO;
    #ifdef DEBUG
		freopen("p.in", "r", stdin);
		freopen("p.out", "w", stdout);
	#endif
    int n, realMp, idk; cin>>n;
    vector<int> buf(n);
    for (auto i=0; i<n;i++){
        cin>>realMp;
        ans[i] = realMp-1;
    }
    while (cin>>idk) {
        buf[ans[0]] = idk;
        for (auto i=1; i<n;i++) {
            cin>>idk;
            buf[ans[i]] = idk;
        }
        vector<int> lis;
        lis.pb(buf[0]);
        for(int i = 0; i < buf.size(); i++) 
            for(int j = 0; j < i; j++) if(buf[j] < buf[i])
                lis[i] = max(lis[i], lis[j] + 1);
        cout<<*max_element(lis.begin(), lis.end())<<endl;
    }
    return EXIT_SUCCESS;
}
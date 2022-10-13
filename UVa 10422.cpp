#include <bits/stdc++.h>
#define endl "\n"
#define endll "\n\n"
#define IO ios_base::sync_with_stdio(0);cin.tie(0)
#define ll long long
#define inf 0x3f3f3f3f
#define MAXN maxn
#define MODN modn

using namespace std;

string ed  = "111110111100 110000100000";
set<string> book;
class node {
    public:
        node(string s="", int cnt = 0): s(s), cnt(cnt) {}
        string s;
        int cnt;
};

int bfs(node st){
    queue<node> que;
    que.push(st);
    while (!que.empty()){
        node cur = que.front();
        que.pop();
        if (cur.s == ed) return cur.cnt;
        if (cur.cnt>9) continue;
        int canGo = cur.s.find(' '), cRow=canGo/5, cCol=canGo%5;
        for (int i=-2; i<=2; i++){
            for (int j=-2; j<=2; j++){
                if (abs(i)==abs(j) || !i || !j) continue;
                if (cRow+i<0 || cRow+i>4 || cCol+j<0 || cCol+j>4) continue;
                int pos = (cRow+i)*5+cCol+j;
                node tmp = cur;
                swap(tmp.s[pos], tmp.s[canGo]);
                if (book.count(tmp.s)) continue;
                book.insert(tmp.s);
                tmp.cnt++;
                que.push(tmp);
                if (tmp.s == ed) return tmp.cnt;
            }
        }
    }
    return 11;
}

signed main(){
    IO;
    #ifdef DEBUG
		freopen("p.in", "r", stdin);
		freopen("p.out", "w", stdout);
	#endif

    int n;
    string tmp;
    cin>>n; getline(cin, tmp);
    while (n--) {
        string s;
        book.clear();
        for (int i=0;i<5;i++){
            getline(cin, tmp);
            tmp = tmp.substr(0, 5);
            s+=tmp;
        }
        node st(s, 0);
        int res = bfs(st);
        if (res<11) cout<<"Solvable in "<<res<<" move(s)."<<endl;
        else cout<<"Unsolvable in less than 11 move(s)."<<endl;

    }

    return EXIT_SUCCESS;
}

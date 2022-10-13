#include <bits/stdc++.h>
#define endl "\n"
#define endll "\n\n"
#define pb emplace_back
#define IO ios_base::sync_with_stdio(0);cin.tie(0);cout.sync_with_stdio(0)
#define ll long long
#define inf 0x3f3f3f3f
#define MAXN 20005
#define MODN modn

using namespace std;

struct book{
    string title;
    string author;
    bool operator == (const book &b) const{
        return title == b.title && author == b.author;
    }
};

bool comp(book a, book b) {	//
    if (a.author == b.author)
        return a.title < b.title;
    return a.author < b.author;
}

signed main(){
    //IO;
    #ifdef DEBUG
		freopen("p.in", "r", stdin);
		freopen("p.out", "w", stdout);
	#endif
    
    vector<book> list, ret;
    map<string, string> backups;
    string s;
    while (getline(cin, s) && s!="END"){
        book tmp;
        int pos = s.find('\"', 1);
        tmp.title = s.substr(0, pos+1);
        tmp.author = s.substr(pos+1, s.size()-1);
        list.pb(tmp);
        backups[tmp.title] = tmp.author;
    }
    while (cin>>s && s!="END"){
        if (s == "SHELVE") {
			sort(ret.begin(), ret.end(), comp);
			for (int i = 0;i < ret.size();i++) {
				book tmp = ret[i];
				list.push_back(tmp);
				sort(list.begin(), list.end(), comp);
				for (int i = 0;i < list.size();i++) {
					if (list[i] == tmp) {
						if (i==0)cout << "Put " << tmp.title << " first" << endl;
						else cout << "Put " << tmp.title << " after " << list[i-1].title << endl;
						break;
					}
				}
			}
			ret.clear();
			cout << "END" << endl;
		}
		else {
            book tmp;
            string bow;
			getchar();
			getline(cin, bow);
			tmp.title = bow;
			tmp.author = backups[bow];
			if (s == "BORROW")
				list.erase(find(list.begin(), list.end(), tmp));
			else if (s == "RETURN") 
                ret.pb(tmp);
		}
    }
    return EXIT_SUCCESS;
}

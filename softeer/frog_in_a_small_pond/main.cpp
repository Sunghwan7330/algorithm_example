#include<iostream>
#include<vector>

using namespace std;

unsigned int gMemberWeight[100000] = {0, };

int main(int argc, char** argv)
{
	
	int n, m;
	int i, j;
	int a, b;
	int check;
	int myWeight, orderWeight;
	int res = 0;

	cin >> n >> m;
	for(i=0; i<n; i++)  cin >> gMemberWeight[i];

	vector<vector<int>> memberVec(n);
	for (i=0; i<m; i++) {
		cin >> a >> b;
		a -= 1;
		b -= 1;
		memberVec[a].push_back(b);
		memberVec[b].push_back(a);
	}

	for (i=0; i<n; i++) {
		//cout << memberVec[i].size() << endl;
		check = 1;
		myWeight = gMemberWeight[i];
		for(j=0; j<memberVec[i].size(); j++) {
			orderWeight = gMemberWeight[memberVec[i][j]];
			if (myWeight <= orderWeight) {
				check = 0;
				break;
			}
		}
		if (check) res++;
	}
	cout << res << endl;
	return 0;
}
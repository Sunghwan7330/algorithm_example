#include<iostream>
#include<vector>
#include<algorithm>
//#include<queue>

using namespace std;

int main(int argc, char** argv)
{
	int i;
	int w, n;
	int weight, price;
	int nowWeight = 0;
	int nowPrice = 0;
	vector<vector<int>> gemsVec;
	cin >> w >> n;

	for(i=0; i<n; i++) {
		cin >> weight >> price;
		gemsVec.push_back(vector<int>{price, weight});
	}

	sort(gemsVec.begin(), gemsVec.end(), greater<vector<int>>());

	for(i=0; i<n; i++) {
		weight = gemsVec[i][1];
		price = gemsVec[i][0];
		if (nowWeight + weight > w) {
			nowPrice += (w-nowWeight) * price;
			nowWeight += w-nowWeight; 		
			break;
		}
		else {
			nowWeight += weight;
			nowPrice += price*weight;
		}
	}
	cout << nowPrice << endl;

	return 0;
}
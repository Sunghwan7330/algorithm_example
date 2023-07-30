#include<iostream>


using namespace std;

int main(int argc, char** argv)
{
	int n, i, j, cnt;
	int maxVal = 0;
	unsigned int bridgeArr[3000] = {0, };
	unsigned int dpArr[3000] = {0, };

	cin >> n;

	for(i=0; i<n; i++) {
		cin >> bridgeArr[i];
		dpArr[i] = 1;
	}

	for(i=0; i<n; i++) {
		cnt = 0;
		for(j=0; j<i; j++) {
			if (bridgeArr[i] > bridgeArr[j]) {
				cnt = dpArr[j] > cnt ? dpArr[j] : cnt;
			}
		}
		cnt++;
		dpArr[i] = cnt;
		maxVal = cnt > maxVal ? cnt : maxVal;
	}

	cout << maxVal << endl;
	return 0;
}
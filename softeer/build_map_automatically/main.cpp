#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int n;
	int i;
	int res = 2;

	cin >> n;

	for (i=0; i<n; i++) {
		res = res * 2 - 1;
	}

	cout << res * res << endl;
	

	return 0;
}
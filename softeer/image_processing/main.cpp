#include<iostream>


using namespace std;

int h, w;
int mapArr[128][128] = {0, };

const int dx[] = {1, -1, 0, 0};
const int dy[] = {0, 0, 1, -1};

void printMap() {
	int i, j;
	for (i=0; i<h; i++) {
		for (j=0; j<w; j++) {
			cout << mapArr[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void paintColor(int x, int y, int color) {
	int nx, ny;
	int i;
	int old_color = mapArr[x][y];

	mapArr[x][y] = color;

	for(i=0; i<4; i++) {
		nx = x + dx[i];
		ny = y + dy[i];

		if (nx < 0 || nx >= h) continue;
		if (ny < 0 || ny >= w) continue;
		if (mapArr[nx][ny] != old_color) continue;
		paintColor(nx, ny, color);
	}
}

int main(int argc, char** argv)
{
	int i, j;
	int n;
	int x, y, c;

	cin >> h >> w;
	for (i=0; i<h; i++) {
		for (j=0; j<w; j++) {
			cin >> mapArr[i][j];
		}
	}

	cin >> n;

	for(i=0; i<n; i++) {
		cin >> x >> y >> c;
		x -= 1;
		y -= 1;

		if (mapArr[x][y] != c)
			paintColor(x, y, c);
	}

	printMap();


	return 0;
}
#include <stdio.h>
#include <string.h>

#define TRUE  1
#define FALSE 0

char board[5][5];

char word_arr[50][11];
int cache_arr[5][5][10];

const int dx[8] = {-1, -1, -1,  1,  1,  1,  0,  0};
const int dy[8] = {-1,  0,  1, -1,  0,  1, -1,  1};

int hasWord(int y, int x, char* word, int depth) {
	int dir;
	int nextX, nextY;

	if (*(word+1) == '\0') return TRUE;

	for (dir=0; dir<8; dir++) {
		nextY = y + dy[dir];
		nextX = x + dx[dir];
		if (nextY < 0 || nextY >= 5)	continue;
		if (nextX < 0 || nextX >= 5)	continue;

		if (board[nextY][nextX] != *(word+1)) continue;
		if (cache_arr[nextY][nextX][depth] == 1) continue;

		if(hasWord(nextY, nextX, word+1, depth+1)){
			return TRUE;
		}
	}

	if (depth > 0){
		cache_arr[y][x][depth-1] = 1;
	}
	return FALSE;
}

int main(){
	int cnt;
	int N;
	int i, j, k, n;
	int flag;

	scanf("%d", &cnt);

	for(n=0; n<cnt; n++){

		for (i=0; i<5; i++) {
			scanf("%s", &board[i]);
		}
		scanf("%d", &N);

		for (i=0; i<N; i++) {
			scanf("%s", &word_arr[i]);
		}

		for(k=0; k<N; k++){
			flag = FALSE;
			for(i=0; i<5; i++){
				for(j=0; j<5; j++){
					if (board[i][j] != word_arr[k][0])
						continue;
					memset(cache_arr, 0x00, sizeof(cache_arr));
					if(hasWord(i, j, word_arr[k], 0)){
						flag = TRUE;
						break;
					}
				}
			}
			if (flag)
				printf("%s YES\n", word_arr[k]);
			else
				printf("%s NO\n", word_arr[k]);
		}
	}
	return 0;
}

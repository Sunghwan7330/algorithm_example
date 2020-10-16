#include<stdio.h>
#include<string.h>

#define MAX_SIZE 100
int n;
int board[MAX_SIZE][MAX_SIZE];
int cache[MAX_SIZE][MAX_SIZE];

int jump(int y, int x){
	int ret;
	int jumpSize;
	if (y >= n || x >= n)
		return 0;

	if (y == n-1 && x == n-1)
		return 1;
	
	ret = cache[y][x];

	if(ret != -1)
		return ret;
	
	jumpSize = board[y][x];

	ret = (jump(y + jumpSize, x) || jump(y, x + jumpSize));

	cache[y][x] = ret;
	return ret;
}


void printBoard(){
	int i, j;

	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			printf("%d ", board[i][j]);
		}
		printf("\n");
	}
}

int main(){
	int c, cnt;
	int i, j;

	scanf("%d", &cnt);
	for(c=0; c<cnt; c++){
		memset(cache, 0xff, sizeof(int) * MAX_SIZE * MAX_SIZE);
		scanf("%d", &n);
		for(i=0; i<n; i++){
			for(j=0; j<n; j++){
				scanf("%d", &board[i][j]);
			}
		}
		//printBoard(n);
		if(jump(0, 0) == 1)
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}

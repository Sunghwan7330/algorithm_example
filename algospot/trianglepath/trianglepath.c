#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100

int n;
int triangle[MAX_SIZE][MAX_SIZE];
int cache[MAX_SIZE][MAX_SIZE];

int path(int y, int x){
	int ret;
	int r1, r2;

	if (y == n-1)
		return triangle[y][x];
	
	ret = cache[y][x];
	if (ret != -1)
		return ret;
	
	r1 = path(y+1, x);
	r2 = path(y + 1, x + 1);

	ret = r1 > r2 ? r1 : r2;
	ret += triangle[y][x];
	cache[y][x] = ret;

	return ret;
}

int main(){
	int c, cnt;
	int i, j;


	scanf("%d", &cnt);

	for(c=0; c<cnt; c++){
		scanf("%d", &n);
		memset(cache, 0xff, sizeof(int) * MAX_SIZE * MAX_SIZE);
		for(i=0; i<n; i++){
			for(j=0; j<i+1; j++){
				scanf("%d", &triangle[i][j]);
			}
		}
		printf("%d\n", path(0, 0));
	}
	return 0;
}

#include <stdio.h>
#include <string.h>

#define MAX_SIZE 500

int n;
int cache[MAX_SIZE];
int S[MAX_SIZE];

int lis(int start){
	int ret, r;
	int next;
	ret = cache[start];

	if (ret != -1)
		return ret;

	ret = 1;	
	for(next = start+1; next < n; next++){
		if(S[start] < S[next]){
			r = lis(next) + 1;
			ret = ret > r ? ret : r;
		}
	}
	cache[start] = ret;
	return ret;
}

int main(){
	int c, cnt;
	int i;
	int res, max;

	scanf("%d", &cnt);

	for(c=0; c<cnt; c++){
		memset(cache, 0xff, sizeof(int) * MAX_SIZE);
		max = 0;
		scanf("%d", &n);
		for(i=0; i<n; i++){
			scanf("%d", &S[i]);
		}
		for(i=0; i<n; i++){
			res = lis(i);
			max = max > res ? max : res;
		}
		printf("%d\n", max);
	}

	return 0;
}

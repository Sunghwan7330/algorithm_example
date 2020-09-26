#include <stdio.h>

#define MAX_FENCE 20480

#define max(a, b) (((a) > (b)) ? (a) : (b))
#define min(a, b) (((a) < (b)) ? (a) : (b))

int h[MAX_FENCE];

int solve(int left, int right){
	int mid;
	int ret;
	int lo, hi;
	int height;

	if (left == right)  return h[left];
	
	mid = (left + right) / 2;

	ret = max(solve(left, mid), solve(mid+1, right));

	lo = mid;
	hi = mid + 1;
	height = min(h[lo], h[hi]);

	ret = max(ret, height * 2);
	
	while(left < lo || hi < right){
		if(hi < right && (lo == left || h[lo-1] < h[hi + 1])) {
			hi++;
			height = min(height, h[hi]);
		}
		else{
			lo--;
			height = min(height, h[lo]);
		}
		ret = max(ret, height * (hi - lo + 1));
	}

	return ret;
}

int main(){
	int c, n, cnt;
	int i;
	int fence[20480];
	scanf("%d", &cnt);

	for(c=0; c<cnt; c++){
		scanf("%d", &n);
		for(i=0; i<n; i++){
			scanf("%d", &h[i]);
		}
		printf("%d\n", solve(0, n-1));
	}

	return 0;
}

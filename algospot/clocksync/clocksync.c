#include <stdio.h>

#define TRUE 1
#define FALSE 0

#define INF 9999
#define SWITCHS 10
#define CLOCKS 16

int linked[SWITCHS][CLOCKS] = {
//{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5}
	{1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0},
	{0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1},
	{1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0},
	{1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1},
	{0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1},
	{0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1},
	{0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0}
};

int min(int a, int b){
	if(a < b)
		return a;

	return b;
}

void push(int clocks[], int swtch){
	int i;
	for(i=0; i<CLOCKS; i++){
		if(linked[swtch][i] == 1){
		clocks[i] += 3;
		if(clocks[i] == 15)
			clocks[i] = 3;
		}
	}
}

int solve(int clocks[], int swtch){
	int ret = INF;
	int i;
	int flag = TRUE;
	int temp;

	if(swtch == SWITCHS){
		for(i=0; i<CLOCKS; i++){
			if(clocks[i] != 12){
				flag = FALSE;
				break;
			}
		}
		if(flag == TRUE)
			return 0;
		else
			return INF;
	}
	
	for(i=0; i<4; i++){
		temp = i + solve(clocks, swtch + 1);
		if(temp < ret)
			ret = temp;
		push(clocks, swtch);
	}
	return ret;
}

int main(){
	int n, cnt;
	int clock_arr[16];
	int i, j;
	int ret;
	scanf("%d", &cnt);
	
	for(n=0; n<cnt; n++){
		for(i=0; i<16; i++)
			scanf("%d", &clock_arr[i]);

		ret = solve(clock_arr, 0);
		if (ret >= INF)		ret = -1;
		printf("%d\n", ret);
	}

	return 0;
}


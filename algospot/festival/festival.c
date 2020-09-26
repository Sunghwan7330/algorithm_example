#include <stdio.h>
#include <string.h>

int main(){
	int cnt, tc_cnt;
	int i, j, k;
	int n, l;
	int costs[1000];
	unsigned int sum_arr[1000];
	unsigned int sum;
	double price, min_price;
	double answer_arr[100];

	scanf("%d", &tc_cnt);

	for(cnt=0; cnt<tc_cnt; cnt++){
		memset(&sum_arr, 0xff, sizeof(sum_arr));
		min_price = 100;

		scanf("%d %d", &n, &l);
		for (i=0; i<n; i++){
			scanf("%d", &costs[i]);
		}

		for (i=0; i<n-l+1; i++){
			price = 0;
			sum = 0;
			k = 0;
			for(j=i; j<n; j++){
				sum += costs[j];
				if (sum_arr[k] > sum){
					sum_arr[k] = sum;
				}
				k++;
			}
		}
		for (i=l-1; i<n; i++){
			price = (double)sum_arr[i] / (double)(i+1);
			//printf("%d - sum : %d, %f\n", i, sum_arr[i], price);
			if(min_price > price)
				min_price = price;
		}
		answer_arr[cnt] = min_price;
	}
	for(i=0; i<tc_cnt; i++)
		printf("%.10f\n", answer_arr[i]);
}

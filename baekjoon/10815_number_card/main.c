#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
	char* checkarr;
	int n, m, tmp, v;
	int i;
	
	checkarr = (char*)malloc(sizeof(char) * 10000001);
	memset(checkarr, 0x00, sizeof(char) * 10000001);
	
	scanf("%d", &n);
	for(i=0; i<n; i++){
		scanf("%d", &tmp);
		if (tmp >= 0)
			checkarr[tmp] |= 0x01;
		else {
			tmp *= -1;
			checkarr[tmp] |= 0x02;
		}
	}
	
	scanf("%d", &m);
	for(i=0; i<m; i++){
		tmp = 0;
		scanf("%d", &v);
		if (v < 0){
			v *= -1;
			tmp = 1;
		}
			
		if (tmp == 0) {
			if(checkarr[v] & 0x01 == 0x01) {
				printf("1 ");
			}
			else {
				printf("0 ");
			}
		}
		else {
			if((checkarr[v] & 0x02) == 0x02) {
				printf("1 ");
			}
			else {
				printf("0 ");
			}
		}
	}
	
	return 0;
}
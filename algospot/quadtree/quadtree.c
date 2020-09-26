#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STR 1024

char temp_res[MAX_STR];

char* it;

int reverse() {
	char* ret_ptr;
	int ret1, ret2, ret3, ret4;
	int ret_sum = 0;
	char* tmp1;
	char* tmp2;
	char* tmp3;
	char* tmp4;

	char head = *it;
	it++;

	if (head == 'b' || head == 'w'){
		temp_res[0] = head;
		return 1;
	}

	ret1 = reverse();
	tmp1 = (char*)malloc(sizeof(char) * ret1);
	memcpy(tmp1, temp_res, ret1);

	ret2 = reverse();
	tmp2 = (char*)malloc(sizeof(char) * ret2);
	memcpy(tmp2, temp_res, ret2);

	ret3 = reverse();
	tmp3 = (char*)malloc(sizeof(char) * ret3);
	memcpy(tmp3, temp_res, ret3);

	ret4 = reverse();
	tmp4 = (char*)malloc(sizeof(char) * ret4);
	memcpy(tmp4, temp_res, ret4);

	temp_res[0] = 'x';
	ret_sum += 1;
	memcpy(temp_res + ret_sum, tmp3, ret3);
	ret_sum += ret3;
	memcpy(temp_res + ret_sum, tmp4, ret4);
	ret_sum += ret4;
	memcpy(temp_res + ret_sum, tmp1, ret1);
	ret_sum += ret1;
	memcpy(temp_res + ret_sum, tmp2, ret2);
	ret_sum += ret2;

	free(tmp1);
	free(tmp2);
	free(tmp3);
	free(tmp4);

	return ret_sum;
	
}

int main(){
	int i, cnt;
	int res;
	char input[MAX_STR];
	scanf("%d", &cnt);


	for(i=0; i<cnt; i++){
		scanf("%s", input);
		it = input;
		res = reverse();
		temp_res[res] = '\0';	
		printf("%s\n", temp_res);
	}

}

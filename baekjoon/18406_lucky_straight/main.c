#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
	char input[16];
	int i;
	int sum1 = 0, sum2 = 0;
	int half;
	
	scanf("%s", input);
	half = strlen(input) / 2;
	
	for (i=0; i<half; i++) {
		sum1 += input[i] & 0x0f;
		sum2 += input[i+half] & 0x0f;
	}
	
	if (sum1 == sum2)
		printf("LUCKY\n");
	else
		printf("READY\n");
	
	return 0;
}
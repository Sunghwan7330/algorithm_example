#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int a, b;
    char* arr;
    int i, n;

    scanf("%d %d", &a, &b);
    if (a < 2)
        a = 2;

    arr = (char*)malloc(sizeof(char) * (b+1));
    memset(arr, 0x00, sizeof(char) * (b+1));

    for(i=2; i<b+1; i++) {
        if (arr[i] == 0) {
            n = i + i;
            while(n < b+1) {
                arr[n] = 1;
                n += i;
            }
        }
    }

    for(i=a; i<b+1; i++) {
        if(!arr[i]) {
            printf("%d\n", i);
        }
    }

    free(arr);
    return 0;
}
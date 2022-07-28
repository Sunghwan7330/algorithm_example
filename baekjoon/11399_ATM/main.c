#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;    // 오름차순
}

int main() {
    int n;
    int arr[1024];
    int i;
    int sum = 0, res = 0;

    scanf("%d", &n);

    for (i=0; i<n; i++) {
        scanf("%d", &arr[i]);
        
    }

    qsort(arr, n, sizeof(int), compare);

    for (i=0; i<n; i++) {
        sum = sum + arr[i];
        res += sum;
    }

    printf("%d\n", res);
}
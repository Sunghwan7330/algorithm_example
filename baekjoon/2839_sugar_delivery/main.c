#include <stdio.h>

int main() {
    int n;
    int a, b, q;

    scanf("%d", &n);
    
    a = (int)n / 5;
    b = n % 5;
    q = b % 3;

    while(q != 0 && a >= 0) {
        a--;
        b += 5;
        q = b % 3;
    }
    if (a<0)
        printf("-1\n");
    else
        printf("%d\n", a + ((int)b/3));
    
}
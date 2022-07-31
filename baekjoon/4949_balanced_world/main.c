#include <stdio.h>

char stack[128];
int idx = 0;

int push(char val){
    stack[idx] = val;
    idx++;
    return 1;
}
char pop() {
    char res = stack[idx-1];
    idx--;
    return res;
}

int isPair(char a, char b) {
    //printf("%c %c\n", a, b);
    if (a == '(' && b == ')' ) return 1;
    else if (a == '[' && b == ']' ) return 1;

    return 0;
}

int solution() {
    char msg[128];
    char val;
    char tmp;
    int i = 0;
    idx = 0;
    
    gets(msg);
    //printf("%s\n", msg);

    if (msg[0] == '.')  return 0;

    while(msg[i] != '.') {
        val = msg[i];
        //printf("%c ", val);
        if (val == '(' || val == '[')
            push(val);
        else if (val == ')' || val == ']') {
            if (idx == 0)  return -1;
            tmp = pop();
            if (!isPair(tmp, val)) return -1;
        }
        i++;
    }

    if (idx != 0)
        return -1;

    return 1;
}

int main() {
    int res;
    while(1) {
        res = solution();
        if (res == 0)  break;

        if (res == 1)  printf("yes\n");
        else printf("no\n");
    }

    return 0;
}
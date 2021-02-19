#include <stdio.h>
#include <string.h>

#define TRUE  1
#define FALSE 0
#define MAX_FILE_CNT (50)
#define MAX_FILE_LEN (100)

// https://dojang.io/mod/page/view.php?id=637
void bubble_sort(char* arr[], int count) {
	int i, j;
	char* temp;

	for (i = 0; i < count; i++) {
		for (j = 0; j < count - 1; j++) {
			if(strcmp(arr[j], arr[j+1]) > 0){
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

int match(char* w, int w_size, char* s, int s_size) {
 	int pos = 0;
	int skip;

	while(pos < s_size && pos < w_size && 
				(w[pos] == '?' || w[pos] == s[pos]) )
		pos++;

	if(pos == w_size){
		return pos == s_size;
	}

	if(w[pos] == '*'){
		if(pos + 1 == w_size)
			return TRUE;
		for(skip = 0; pos + skip < s_size; skip++){
			if(match(w + (pos+1), w_size-(pos+1), s + (pos + skip), s_size - (pos + skip)))
				return TRUE;
		}
	}

	return FALSE;
}

int main(){
	int c, cnt;
	int n, num;
	char target[MAX_FILE_LEN + 1];
	char words[MAX_FILE_CNT][MAX_FILE_LEN + 1];
	int target_len, word_len;
	int ret, answer_cnt;
  char* answer_arr[MAX_FILE_CNT];

	scanf("%d", &cnt);

	for(c=0; c<cnt; c++){
		scanf("%s", target);
		target_len = strlen(target);
		scanf("%d", &num);

		memset(answer_arr, 0, sizeof(char*) * MAX_FILE_CNT);
		answer_cnt = 0;
		for(n=0; n<num; n++){
			scanf("%s", words[n]);
			word_len = strlen(words[n]);
			ret = match(target, target_len, words[n], word_len);
			if(ret){
				answer_arr[answer_cnt++] = words[n];
			}
		}
		bubble_sort(answer_arr, answer_cnt);
		for(n=0; n<answer_cnt; n++){
			printf("%s\n", answer_arr[n]);
		}
	}

	return 0;
}

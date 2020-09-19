#include <stdio.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int n;
int areFriends[10][10];

int countPairings(int taken[10]) {
	int firstFree = -1;
	int i;
	int ret = 0;
	int pairWith;

	for (i=0; i<n; i++) {
		if (!taken[i]) {
			firstFree = i;
			break;
		}
	}

	if (firstFree == -1) return 1;

	for (pairWith = firstFree + 1; pairWith < n; pairWith++) {
		if (!taken[pairWith] && areFriends[firstFree][pairWith]) {
			taken[firstFree] = taken[pairWith] = TRUE;
			ret += countPairings(taken);
			taken[firstFree] = taken[pairWith] = FALSE;
		}
	}
	return ret;
}

int processPairings(){
	int i;
	int m;
	int fa, fb; //friend_a, friend_b
	int taken[10];

	// init
	memset(areFriends, 0x00, sizeof(areFriends));
	memset(taken, 0x00, sizeof(taken));

	scanf("%d %d", &n, &m);

	for (i=0; i<m; i++){
		scanf("%d %d", &fa, &fb);
		areFriends[fa][fb] = 1;
		areFriends[fb][fa] = 1;
	}
	printf("%d\n", countPairings(taken));
}

int main(){
	int c, i;

	scanf("%d", &c);

	for(i=0; i<c; i++)
		processPairings();

	return 0;
}

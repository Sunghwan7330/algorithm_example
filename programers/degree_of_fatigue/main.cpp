#include <string>
#include <vector>

using namespace std;

int maxCnt = 0;

int visitArr[8] = {0, };
void dfs(int k, vector<vector<int>> dungeons, int cnt) {
    int i;
    
    for(i=0; i<dungeons.size(); i++) {
        if (visitArr[i] == 0 && dungeons[i][0] <= k) {
            visitArr[i] = 1;
            dfs(k-dungeons[i][1], dungeons, cnt + 1);
            visitArr[i] = 0;
        }
    }
    maxCnt = maxCnt < cnt ? cnt : maxCnt;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    dfs(k, dungeons, 0);
    return maxCnt;
}
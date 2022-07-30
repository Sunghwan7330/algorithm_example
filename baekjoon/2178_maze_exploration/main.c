#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n, m;

char maze[101][101] = {0, };
unsigned int visit[101][101] = {0, };

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int dfs(int x, int y, int dis) {
    int i;
    int nx, ny;

    if (visit[x][y] <= dis)
        return 0;
    visit[x][y] = dis;

    for (i=0; i<4; i++) {
        nx = x + dx[i];
        ny = y + dy[i];
        if (nx < 0) continue;
        if (nx >= n) continue;
        if (ny < 0) continue;
        if (ny >= m) continue;
        if (maze[nx][ny] == '0') continue;
        dfs(nx, ny, dis+1);
    }
}

int main() {


    int i, j;

    scanf("%d %d", &n, &m);
    
    for(i=0; i<n*m; i++) {
        scanf("%s", maze[i]);
    }
    for (i=0; i<n; i++) {
        for(j=0; j<m; j++) {
            visit[i][j] = 9999999;
        }
    }
    
    dfs(0, 0, 1);

    printf("%d\n", visit[n-1][m-1]);

    return 0;
}
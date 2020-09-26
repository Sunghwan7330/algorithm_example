#include <stdio.h>
#include <string.h>

#define TRUE  1
#define FALSE 0

const int coverType[4][3][2] = {
  { {0, 0}, {1, 0}, {0, 1} }, // (b)
  { {0, 0}, {0, 1}, {1, 1} }, // (c)
  { {0, 0}, {1, 0}, {1, 1} }, // (d)
  { {0, 0}, {1, 0}, {1, -1} } // (e)
};

int h, w; // height, width
int  board[20][20];

void print_board(){
  int i, j;

  for(i=0; i<h; i++){
    for(j=0; j<w; j++){
      printf("%d", board[i][j]);
    }
    printf("\n");
  }
}

int set(int y, int x, int type, int delta) {
  int ok = TRUE;
  int i;
  int ny, nx;


  for(i=0; i<3; i++) {
    ny = y + coverType[type][i][0];
    nx = x + coverType[type][i][1];

    if (ny < 0 || ny >= h || nx < 0 || nx >= w)
      ok = FALSE;
    else if ((board[ny][nx] += delta) > 1)
      ok = FALSE;
  }

  //printf("set - delta : %d, type : %d\n", delta, type);
  //print_board();
  return ok;
}

int cover(){
  int y = -1, x = -1;
  int i, j;
  int ret, type;
  //printf("cover - \n");
  //print_board();

  for(i=0; i<h; i++){
    for(j=0; j<w; j++){
      if (board[i][j] == 0) {
        y = i;
        x = j;
        break;
      }
    }
    if (y != -1)  break;
  }
  //printf("%d, %d\n", y, x);
  if (y == -1)  return 1;
  ret = 0;
  for(type=0; type < 4; type++) {
    if (set(y, x, type, 1))
      ret += cover();
    set(y, x, type, -1);
  }
  return ret;
}

int process_boardcover(){
  int i, j;
  char board_str[20][21];
  scanf("%d %d", &h, &w);

  for(i=0; i<h; i++){
    scanf("%s", board_str[i]);
  }

  for(i=0; i<h; i++){
    for(j=0; j<w; j++){
      if (board_str[i][j] == '#') 
        board[i][j] = 1;
      else
        board[i][j] = 0;
    }
  }

  printf("%d\n", cover());

  return 0;
}

int main(){
  int c, i;

  scanf("%d", &c);
  for (i=0; i<c; i++){
    process_boardcover();
  }
  return 0;
}

#include <string>
#include <vector>

#define MAX_VAL (999)

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    int keymapArr[26];
    int i, j;
    int sum;
    
    for(i=0; i<26; i++) keymapArr[i] = MAX_VAL;
    
    for(i=0; i<keymap.size(); i++) {
        for(j=0; j<keymap[i].length(); j++) {
            if (keymapArr[keymap[i][j]-65] > j) {
                keymapArr[keymap[i][j]-65] = j+1;
            }
        }
    }
    
    for(i=0; i<targets.size(); i++) {
        sum = 0;
        for(j=0; j<targets[i].length(); j++) {
            if (keymapArr[targets[i][j]-65] == MAX_VAL) {
                sum = -1;
                break;
            }
            sum += keymapArr[targets[i][j]-65];
        }
        answer.push_back(sum);
    }
    s
    return answer;
}
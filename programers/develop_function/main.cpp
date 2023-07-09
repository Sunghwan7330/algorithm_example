#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int cnt;
    int i;
    
    while(progresses.size() != 0) {
        for(i=0; i<progresses.size(); i++) {
            progresses[i] += speeds[i];
        }
        
        cnt = 0;
        while(progresses.size() != 0 && progresses[0] >= 100) {
            cnt++;
            progresses.erase(progresses.begin());
            speeds.erase(speeds.begin());
        }
        if (cnt != 0) answer.push_back(cnt);
        
    }
    
    return answer;
}
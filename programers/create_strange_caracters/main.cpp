#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int cnt = 0;
    for(int i=0; i<s.length(); i++) {
        if (cnt%2 == 0) {
            if (s[i] >= 'a' &&  s[i] <= 'z') answer += s[i] - 32;
            else answer += s[i];
        }
        else {
            if (s[i] >= 'A' &&  s[i] <= 'Z') answer += s[i] + 32;
            else answer += s[i];
        }
        cnt++;
        if (s[i] == ' ') cnt = 0;
        
    }
    return answer;
}
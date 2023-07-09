#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> nodeVec;
int distanceArr[20000] = {0, };

void printNodeVector() {
    int i, j;
    for(i=0; i<nodeVec.size(); i++) {
        cout << i << " : ";
        for(j=0; j<nodeVec[i].size(); j++) {
            cout << nodeVec[i][j] << " ";
        }
        cout << endl;
    }
}
int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    int i;
    int a, b;
    int nodeIdx, nextIdx;
    int maxDistance = 0;
    vector<int> bfsQueue;
    
    for(i=0; i<n; i++) {
        nodeVec.push_back(vector<int>());
        distanceArr[i] = -1;
    }
    for(i=0; i<edge.size(); i++) {
        a = edge[i][0]-1;
        b = edge[i][1]-1;
        nodeVec[a].push_back(b);
        nodeVec[b].push_back(a);
    }
    
    //printNodeVector();
    distanceArr[0] = 0;
    bfsQueue.push_back(0);
    while(bfsQueue.size() != 0) {
        nodeIdx = bfsQueue[0];
        bfsQueue.erase(bfsQueue.begin());
        maxDistance = distanceArr[nodeIdx] > maxDistance ? distanceArr[nodeIdx] : maxDistance;
        
        for(i=0; i<nodeVec[nodeIdx].size(); i++) {
            nextIdx = nodeVec[nodeIdx][i];
            if (distanceArr[nextIdx] != -1) continue;
            distanceArr[nextIdx] = distanceArr[nodeIdx] + 1;
            bfsQueue.push_back(nextIdx);
        }
    }
    
    for (i=0; i<n; i++) {
        if (maxDistance == distanceArr[i]) answer++;        
    }
    return answer;
}

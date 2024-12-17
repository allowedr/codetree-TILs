#include <iostream>
#include <algorithm>
using namespace std;

#define MAX_N 200

int arr[MAX_N][MAX_N];
int seq[MAX_N];

int n, m;

int GetNum1stRec(int x, int y){
    int num = 0;
    int cnt = 0;

    for(int i = x; i <= x+1; i++){
        for(int j = y; j <= y+1; j++){
        seq[cnt++] = arr[i][j];
    }
    }

    sort(seq, seq + 4);

    for(int i = 3; i >= 1; i--){
        num += seq[i];
    }

    return num;
}

int GetNum2ndRec1(int x, int y){
    int num = 0;
    for(int i = y; i <= y+2; i++){
        num += arr[x][i];
    }

    return num;
}

int GetNum2ndRec2(int x, int y){
    int num = 0;
    for(int i = x; i <= x+2; i++){
        num += arr[i][y];
    }

    return num;
}

int main() {

    int num;
    int max_num = 0;
    
    cin >> n >> m;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> arr[i][j];
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(j+2 >= m) continue;
            num = GetNum2ndRec1(i, j);
            max_num = max(max_num, num);
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(i+2 >= n) continue;
            num = GetNum2ndRec2(i, j);
            max_num = max(max_num, num);
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(i+1 >= n || j+1 >= m) continue;
            num = GetNum1stRec(i, j);
            max_num = max(max_num, num);
        }
    }

    cout << max_num;

    return 0;
}


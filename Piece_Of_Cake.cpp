#include <iostream>
using namespace std;

int main(){
    int n, h, v, max_piece;
    cin >> n >> h >> v;
    max_piece = max(n - h, h) * max(n - v, v) * 4;
    cout << max_piece;
    return 0;
}

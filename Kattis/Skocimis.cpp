#include <iostream>
using namespace std;

int jumps(int a, int b, int c, int m){
	if(b - a == 1 && c - b == 1){
		return m;
	}
	if(b - a == 1){
		return jumps(b, b + 1, c, m + 1);
	}
	if(c - b == 1){
		return jumps(a, a + 1, b, m + 1);
	}
	return std::max(jumps(b, b + 1, c, m + 1), jumps(a, a + 1, b, m + 1));
}

int main(){
	int a, b, c;
	cin >> a >> b >> c;
	cout << jumps(a, b, c, 0);
}
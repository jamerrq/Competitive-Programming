#include <iostream>
#include <math.h>
using namespace std;

int planina(int n){
	if(n == 0)return 2;
	return (int)(planina(n - 1) * 2 - 1);
}

int main() {
	int n;
	cin >> n;
	cout << (int)(pow(planina(n),2));
}
#include<iostream>
using namespace std;

int main(){
	while(true){
		int d, n;
		cin >> d >> n;
		if(d == 0 && n == 0)break;
		int div = d / n;
		int res = d - (n * div);
		cout << div << " " << res << " / " << n << endl;
	}
}

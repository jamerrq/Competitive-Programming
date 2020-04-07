#include <iostream>
using namespace std;

int players(int l, int r, int a){
	if(l == r){
		l += a / 2;
		r += a / 2;
		return l + r;
	}
	if(l > r){
		if(r + a == l){
			return l * 2;
		}
		if(r + a > l){
			a -= l - r;
			r = l;
			l += a / 2;
			r += a / 2;
			return l + r;
		}
		if(r + a < l){
			return (r + a) * 2;
		}
	}else{
		if(r > l){
			if(l + a == r){
				return r * 2;
			}
			if(l + a > r){
				a -= r - l;
				l = r;
				l += a / 2;
				r += a / 2;
				return r + l;
			}
			if(l + a < r){
				return (l + a) * 2;
			}
		}
	}
}

int main(){
	int l, r, a;
	cin >> l >> r >> a;
	cout << players(l,r,a) << endl;
}

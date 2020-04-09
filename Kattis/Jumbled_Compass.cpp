#include <iostream>
#include <math.h>

int main(){
	int n1, n2;
	std::cin >> n1 >> n2;
	if(n1 > n2){
		int d1 = n1 - n2;
		int d2 = (360 - n1) + n2;
		if(d1 == 180)std::cout << 180;
		else if(d1 > d2)std::cout << d2;
		else std::cout << -d1;
	}else{
		int d1 = n2 - n1;
		int d2 = n1 + (360 - n2);
		if(d1 == 180)std::cout << 180;
		else if(d1 > d2)std::cout << -d2;
		else std::cout << d1;
	}
}
# include <iostream>
using namespace std;

int main(){
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++){
		int ingresoN;
		int ingresoP;
		int P;
		cin >> ingresoN >> ingresoP >> P;
		if(ingresoN < ingresoP - P){
			cout << "advertise" << endl;
		}else{
		    if(ingresoN == ingresoP - P){
			cout << "does not matter" << endl;
		    }else{
			  cout << "do not advertise" << endl;
		    }   
		}
	}	
}
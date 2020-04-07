# include <iostream>
using namespace std;
int main(){
    int nums;
    cin >> nums;
    for(int i = 0; i < nums; i++){
        int n;
        cin >> n;
        if(n % 2 == 0){
            cout << n << " is even" << endl;
        }else{
            cout << n << " is odd" << endl;
        }
    }
}
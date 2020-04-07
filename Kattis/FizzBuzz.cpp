# include <iostream>
using namespace std;
int main(){
    int f, b, n;
    cin >> f >> b >> n;
    for(int i = 1; i <= n; i++){
        if(i % f == 0 && i % b == 0)cout << "FizzBuzz" << endl;
        if(i % f == 0 && i % b != 0)cout << "Fizz" << endl;
        if(i % f != 0 && i % b == 0)cout << "Buzz" << endl;
        if(i % f != 0 && i % b != 0)cout << i << endl;
    }
}
#include<iostream>
using namespace std;

string replaceAll(string data)
{
    while(true){
        size_t found1 = data.find("()");
        size_t found2 = data.find("[]");
        if(found1 == string::npos and found2 == string::npos){
            break;
        }else
        {
            if(found1 != string::npos)data.replace(found1, 2, "");
            if(found2 != string::npos)data.replace(found2, 2, "");
        }
        
    }
    return data;
}

int main(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        s = replaceAll(s);
        if(s.length() == 0){
            cout << "Yes" << endl;
        }else
        {
            cout << "No" << endl;
        }
        
    }
    return 0;
}
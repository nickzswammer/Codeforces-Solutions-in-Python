#include<iostream>
using namespace std;
 
int bit(){
 
    int x = 0;
    int n = 0;
    string statements = "";
 
    cin >> n;
 
 
    for (int i = 0; i < n; i++){
 
        string input = "";
        cin >> input;
        if (input == "++X"){
            x += 1;
 
        }
        else if (input == "X++"){
            x +=1;
 
        }
        else if (input == "--X"){
            x -= 1;
 
        }
        else if (input == "X--"){
            x -= 1;
        }
    }
    return x;
 
 
 
}
 
int main()
{
    cout << bit();
    return 0;
}
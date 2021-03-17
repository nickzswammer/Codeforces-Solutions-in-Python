#include <iostream>
#include <fstream>
#include <string>
using namespace std;
 
int nextround(){
    int n,k;
    cin >> n >> k;
 
    int scores[n];
    for (int i=0; i < n; i++){
        cin>> scores[i];
    }
 
    int counter = 0;
    int counts = scores[k-1];
    for (int i=0; i<n; i++){
        if (scores[i] >= counts){
            if(scores[i] != 0){
                counter++;
            }
        }
    }
 
    int zero_counter = 0;
 
    for (int i=0; i <n; i++){
        if (scores[i] == 0){
            zero_counter++;
        }
    }
    if (zero_counter == 2){
        return 3;

    }
    if (zero_counter >= n){
        return 0;
    }
 
    return counter;
 
}
 
int main(){
 
    cout << nextround();
	return 0;
}
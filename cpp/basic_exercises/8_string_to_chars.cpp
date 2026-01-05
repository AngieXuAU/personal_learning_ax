
#include <iostream>
#include <string>

using namespace std;

int main(){
    string user_in;
    
    cout << "This program tells you the length of a string and prints out each character on a new line. Enter a string: ";
    cin >> user_in;

    cout << "The length is " << user_in.length() << ".";

    for(int i = 0; i < user_in.length(); i++){
        cout << "\n" << user_in[i];
    }
}
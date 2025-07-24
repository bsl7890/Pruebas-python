#include <iostream>
using namespace std;

int main(){
    int edad;
    cout << "\nIngrese su edad: ";
    cin >> edad;
    if (edad <=12)
    {
        cout << "Eres un niño";
    }
    else if (edad >= 12 && edad <= 17)
    {   
        cout << "Eres un adolescente";
    }
    else if (edad >= 18 && edad <= 64) 
    {

        cout << "Eres un adulto";
    }
    else
    {
        cout << "Eres un adulto mayor";
    }
    return 0;
}
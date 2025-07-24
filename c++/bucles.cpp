#include <iostream>
using namespace std;

int main(){
    std::string claveSecreta = "admin123";
    std::string clave;
    while (true)
    {
        cout << "Ingrese la clave secreta";
        cin >> clave;
        if (clave == claveSecreta)
        {
            cout << "Clave correcata";
        }
        
    }

    return 0;
}
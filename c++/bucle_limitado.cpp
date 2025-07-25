#include <iostream>
using namespace std;

int main(){
    std::string claveSecreta = "admin123";
    std::string clave;
    int i = 1;
    while (i <= 3)
    {
        cout << "Ingrese la clave secreta";
        cin >> clave;
        if (clave == claveSecreta)
        {
            cout << "Clave correcata\n";
            break;
        }
        else
        {
            cout << "Clave incorrecta\n";
        }
        i++;
    }
    if (clave != claveSecreta) {
    cout << "Acceso bloqueado\n";
    }
    return 0;
}
#include <iostream>
using namespace std;

int main(){
    int nota;
    cout << "Ingrese una nota del 1 al 5: ";
    cin >> nota;

    switch (nota)
    {
    case 1:
        cout << "Muy deficiente";
        break;
    case 2:
        cout << "Insuficiente";
        break;
    case 3:
        cout << "Suficiente";
        break;
    case 4:
        cout << "Bueno";
        break;
    case 5:
        cout << "Excelente";
        break;
    default:
        cout << "Nota inválida";
        break;
    }

    return 0;
}
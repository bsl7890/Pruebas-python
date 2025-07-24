#include <iostream>
using namespace std;

int main(){
    int numero;
    cout << "\nIngrese un numero entero: ";
    cin >> numero;
    if (numero % 2 == 0)
    {
        cout << "El numero: " << numero << " Es par";
    }
    else if (numero % 2 != 0)
    {
        cout << "El numero: " << numero << " Es impar";
    }
    else
    {
        cout << "Ingrese un numero";
    }
    return 0;
    
}
#include <iostream>
using namespace std;

int main(){
    int numero;
    cout << "Ingrese un numero entero: ";
    cin >> numero;
    if (numero % 2 == 0)
    {
        cout << "El numero: " << numero << " Es par";
    }
    else
    {
        cout << "El numero: " << numero << " Es impar";
    }
    return 0;
    
}
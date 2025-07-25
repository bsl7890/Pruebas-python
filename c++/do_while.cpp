#include <iostream>
using namespace std;

int main(){
    int numero;
    do
    {
        cout << "Ingrese la cantidad de producto debe ser mayor a 0 y menor o igual a 100: \n";
        cin >> numero;
        
        if (numero <= 0 || numero > 100) {
            cout << "Número inválido. Intente de nuevo.\n";
        }
    } while (numero <= 0 || numero > 100);

    cout << "cantidad registrada: "<< numero;
    
}
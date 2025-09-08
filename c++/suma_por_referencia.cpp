#include <iostream>
using namespace std;


void Referencia_numero(int &numero1, int &numero2){
    numero1 = numero1 - 5;
    numero2 = numero2 + 5;
}

int main(){
    int numero1;
    int numero2;
    cout << "Ingrese el primero numero: " << endl;
    cin >> numero1;
    cout << "Ingrese el segundo numero: " << endl;
    cin >> numero2;

    Referencia_numero(numero1, numero2);

    cout << "numero referencial del primer numero: " << numero1 << endl;

    cout << "numero referencial del segundo numero: " << numero2 << endl;

    return 0;
}
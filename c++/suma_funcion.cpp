#include <iostream>
using namespace std;


int sumar_numeros(int numero1, int numero2){
    return numero1 + numero2;
}

int main(){
    int numero1;
    int numero2;
    cout << "Ingrese el primero numero: " << endl;
    cin >> numero1;
    cout << "Ingrese el segundo numero: " << endl;
    cin >> numero2;

    int suma_total = sumar_numeros(numero1, numero2);

    cout << "La suma es: " << suma_total << endl;

    return 0;
}
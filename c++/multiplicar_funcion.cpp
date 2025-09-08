#include <iostream>
using namespace std;


void tabla_multiplicar(int numero){
    int i = 1;
    while (i <= 10)
    {
        cout << numero << " * " << i << " = " << (numero * i) << endl;
        i++;
    }
}

int main(){
    int numero;
    cout << "Ingrese un numero para hacer la tabla de multiplicacion del 1 al 10:" << endl;
    cin >> numero;

    tabla_multiplicar(numero);
}
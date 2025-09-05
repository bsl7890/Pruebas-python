#include <iostream>
using namespace std;

int main(){
    int numero;
    int total;
    cout << "Ingrese un numero para hacer la tabla del 1 al 10: ";
    cin >> numero;
    for (int i = 1; i <=10; i++)
    {
        total = numero * i;
        cout << numero << " * " << i << " = " << total << endl;
    }
    return 0;
}
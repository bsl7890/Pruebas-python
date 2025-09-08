#include <iostream>
using namespace std;

int main() {
    int numero;
    cout << "Ingrese un numero para hacer la tabla del 1 al 10: ";
    cin >> numero;

    for (int i = 1; i <= 10; i++) {
        cout << numero << " * " << i << " = " << (numero * i) << endl;
    }

    return 0;
}

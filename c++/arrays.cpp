#include <iostream>
using namespace std;


int main(){
    int numeros[5];
    int suma = 0;
    for(int i = 1; i <= 5; i++){
        std::cout << "Ingrese el numero "<< i << ": " << std::endl;
        std::cin >> numeros[i-1];

    }
    for (int i = 0; i < 5; ++i) {
        suma += numeros[i];
    }
    
    std::cout << "La suma total es: " << suma << std::endl;

    int mayor = numeros[0];
    int menor = numeros[0];

    for (int i = 1; i < 5; i++) {
        if (numeros[i] > mayor) {
            mayor = numeros[i];
        }
        if (numeros[i] < menor) {
            menor = numeros[i];
        }
    }

    cout << "El numero mayor es: " << mayor << endl;
    cout << "El numero menor es: " << menor << endl;
    return 0;

}
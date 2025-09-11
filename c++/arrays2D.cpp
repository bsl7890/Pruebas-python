#include <iostream>
using namespace std;

int main() {
    int numeros[2][2];
    std::cout << std::endl;
    for(int i = 0; i < 2; i++){
        for(int c = 0; c < 2; c++){
            std::cout << "Ingrese el numero para la posicion [" << i << "][" << c << "]: " << std::endl;
            std::cin >> numeros[i][c];
        }
    }
    
    std::cout << "La matriz ingresada es: " << std::endl;
    
    for(int i = 0; i < 2; i++){
        for(int c = 0; c < 2; c++){
            std::cout << numeros[i][c] << " ";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
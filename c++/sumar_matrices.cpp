#include <iostream>
using namespace std;

int main() {
    int A[2][2], B[2][2], C[2][2];
    
    std::cout << endl;

    std::cout << "Ingrese los valores de la primera matriz (A):" << std::endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            std::cout << "A[" << i << "][" << j << "]: ";
            cin >> A[i][j];
        }
    }

    std::cout << "\nIngrese los valores de la segunda matriz (B):" << std::endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            std::cout << "B[" << i << "][" << j << "]: ";
            cin >> B[i][j];
        }
    }

    // Suma de matrices
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }

    std::cout << "\nLa matriz resultante (C = A + B) es:" << std::endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            std::cout << C[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}

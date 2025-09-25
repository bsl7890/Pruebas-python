#include <iostream>
using namespace std;


struct Direccion {
    std::string calle;
    int numero;
    std::string ciudad;
};


struct Alumno {
    std::string nombre;
    int edad;
    float notas[3];
    float promedio;
    Direccion direccion;
};

int main() {
    Alumno alumno[3];
    int sumaNotas = 0;

    for (int i = 0; i < 3; i++){
        std::cout << std::endl;

        std::cout << "Ingrese su nombre" << std::endl;
        getline(cin, alumno[i].nombre);

        std::cout << "Ingrese su edad" << std::endl;
        std::cin >> alumno[i].edad;
        std::cin.ignore();

        std::cout << "Ingrese su calle" << std::endl;
        getline(cin, alumno[i].direccion.calle);

        std::cout << "Ingrese su numero" << std::endl;
        std::cin >> alumno[i].direccion.numero;
        std::cin.ignore();

        std::cout << "Ingrese su ciudad" << std::endl;
        getline(cin, alumno[i].direccion.ciudad);

    }
    for (int i = 0; i < 3; i++){
        int sumaNotas = 0;  

        for (int n = 0; n < 3; n++) {
            std::cout << "Ingrese la nota " << n+1 << " del alumno: " << alumno[i].nombre << std::endl;
            cin >> alumno[i].notas[n];
            sumaNotas += alumno[i].notas[n];
        }
    
        alumno[i].promedio = (float)sumaNotas / 3;
    }
    cin.ignore();

    std::cout << "\n\n=== Resumen de Alumnos Registrados ===" << std::endl;
    for (int i = 0; i < 3; i++){
        std::cout << "\n-- Alumno " << i + 1 << " --" << std::endl;
        std::cout << "Nombre: " << alumno[i].nombre << std::endl;
        std::cout << "Edad: " << alumno[i].edad << std::endl;
        std::cout << "Direccion: " << alumno[i].direccion.calle << " #" << alumno[i].direccion.numero << ", " << alumno[i].direccion.ciudad << std::endl;
        std::cout << "Notas: " << alumno[i].notas[0] << ", " << alumno[i].notas[1] << ", " << alumno[i].notas[2] << std::endl;
        std::cout << "Promedio: " << alumno[i].promedio << std::endl;
    }
    return 0;
}





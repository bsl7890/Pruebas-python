#include <iostream>
using namespace std;

struct Alumno {
    std::string nombre;
    int edad;
    float promedio;
};
struct Producto{
    std::string nombre_producto;
    float precio;
    int stock;
};
int main() {
    Alumno estudiante;
    Producto producto;
    
    estudiante.nombre = "benjamin";
    estudiante.edad = 18;
    estudiante.promedio = 6.5;
    
    std::cout << "Ingrese el nombre del producto: " << std::endl;
    std::cin >> producto.nombre_producto;
    

    std::cout << endl;
    std::cout << "Nombre: " << estudiante.nombre << std::endl;
    std::cout << "Edad: " << estudiante.edad << std::endl;
    std::cout << "Promedio: " << estudiante.promedio << std::endl;
}
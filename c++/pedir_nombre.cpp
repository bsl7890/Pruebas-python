#include <iostream>
using namespace std;

int main(){

    std::string nombre;
    int edad;
    float altura;
    int dia;
    cout << "Ingrese su nombre:" << endl;
    getline(cin, nombre);

    cout << "Cuantos años tienes" << endl;
    cin >> edad;

    cout << "Por favor diga su altura ej: 1.75" << endl;
    cin >> altura;

    cout << "Hola " << nombre << ", bienvenido a C++!." << endl;
    cout << "Tienes " << edad << " años y mides " << altura << " metros." << endl;

    cout << "Ingrese un numero del 1 al 7" << endl;
    cin >> dia;

    if (cin.fail()) {
        cout << "Debes ingresar un numero, no letras." << endl;
        return 0;
    }

    if (dia < 1 || dia > 7)
    {
        cout << "Ingrese un numero del 1 al 7" << endl;
        return 0;
    }

    switch (dia)
    {
    case 1:
        cout << "El dia es Lunes" << endl;
        break;
    case 2:
        cout << "El dia es Martes" << endl;
        break;
    case 3:
        cout << "El dia es Miercoles" << endl;
        break;
    case 4:
        cout << "El dia es Jueves" << endl;
        break;
    case 5:
        cout << "El dia es Viernes" << endl;
        break;
    case 6:
        cout << "El dia es Sabado" << endl;
        break;
    case 7:
        cout << "El dia es Domingo" << endl;
        break;
    }
    return 0;
    


}
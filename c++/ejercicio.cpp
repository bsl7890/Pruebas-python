#include <iostream>
using namespace std;

int main(){
    std::string nombre;
    int edad;
    float bonificacion = 0.0;
    float precioBruto = 0;
    float iva = 0.19;
    float precioNeto = 0;
    float precioIva = 0;
    float PrecioTotal = 0;
    float precioBonificacion = 0;
    int aumentoCargo = 0;
    int opcionRol;
    std::string roles;
    cout << "Ingrese su nombre: ";
    cin >> nombre;
    cout << "Ingrese su edad: ";
    cin >> edad;
    cout << "Ingrese su precio neto: ";
    cin >> precioNeto;
    if(edad < 18)
    {
        cout << "Usted no tiene bonificacion";
        bonificacion = 0;
    }
    else if (edad >= 18 and edad <= 50)
    {
        cout << "Usted tiene bonificacion" << endl;
        bonificacion = 0.25;
    }
    else if ( edad > 50)
    {
        cout << "Usted tiene bonificacion" << endl;
        bonificacion = 0.35;
    }
    else
    {
        cout << "Ingrese una edad valida"  << endl;
        bonificacion = 0;
    }
    while(true)
    {
        cout << "|-------------------------------------|" << endl;
        cout << "|          Seleccione su cargo        |" << endl;
        cout << "|-------------------------------------|" << endl;
        cout << "|  1. Gerente                         |" << endl;
        cout << "|  2. Trabajador                      |" << endl;
        cout << "|  3. Asistente                       |" << endl;
        cout << "|-------------------------------------|" << endl;
        cin >> opcionRol;

    if (cin.fail()) 
    {
        cin.clear();
        cin.ignore(10000, '\n');
        cout << "Entrada inválida. Intente de nuevo.\n";
        continue; // Repite el bucle
    }
        if (opcionRol == 1)
        {
            cout << "Usted selecciono Gerente" << endl;
            roles = "Gerente";
            aumentoCargo = 25000;
            break;
        }
        else if (opcionRol == 2)
        {
            cout << "Usted selecciono Trabajador" << endl;
            roles = "Trabajador";
            aumentoCargo = 10000;
            break;
        }
        else if (opcionRol == 3)
        {
            cout << "Usted selecciono Asistente" << endl;
            roles = "Asistente";
            aumentoCargo = 5000;
            break;
        }
        else
        {
            cout << "Error Por Favor ingrese alguna de las opciones" << endl;
            cout << "Precione cualquier tecla para continuar";
            cin.ignore();
            cin.get();
        }
    }
    precioIva = precioNeto * iva;
    precioBruto = precioIva + precioNeto;
    precioBonificacion = precioNeto * bonificacion;
    
    PrecioTotal = precioBruto - precioBonificacion + aumentoCargo;        
    cout << endl;
    cout << "|-----------------------------------|" << endl;
    cout << "| Resumen:" << endl;
    cout << "| Nombre: " << nombre << endl;
    cout << "| Edad: " << edad << endl;
    cout << "| Cargo: " << roles << endl;
    cout << "| Precio Neto: $" << precioNeto << endl;
    cout << "| IVA (19%): $" << precioIva << endl;
    cout << "| Precio Bruto (con IVA): $" << precioBruto << endl;
    cout << "| Bonificacion: $" << precioBonificacion << endl;
    cout << "| Aumento por cargo: $" << aumentoCargo << endl;
    cout << "| Precio Total a Pagar: $" << PrecioTotal << endl;
    cout << "|-----------------------------------|" << endl;

    return 0;
}
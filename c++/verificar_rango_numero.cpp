#include <iostream>
using namespace std;

int main(){
    std::string nombre;
    int edad;
    std::string Verificacion;
    std::string permisoEspecia;
    std::string permisoAcceso;
    cout << "Ingrese su nombre: ";
    cin >> nombre;
    cout << "Ingrese su edad: ";
    cin >> edad;
    cout << "Usted tiene carnet de identificacion (s/n): ";
    cin >> Verificacion;
    if (Verificacion != "s" && Verificacion != "n")
    {
        cout << "Por favor ocupe (s/n) para verificar si tiene carnet";
        return 0;
    }
    if (edad < 18)
    {
        cout << "Usted tiene permiso especiales(s/n) ? ";
        cin >> permisoEspecia;
        if (permisoEspecia != "s" && permisoEspecia != "n")
        {
        cout << "Por favor ocupe (s/n) para verificar si tiene carnet";
        return 0;
        }
        if (permisoEspecia == "s" && Verificacion == "s")
        {
            permisoAcceso = "Acceso permitido";
        }
        else
        {
            permisoAcceso = "Acesso denegado";
        }
    }
    else if (edad >=18 && Verificacion == "s")
    {
        permisoEspecia = "n";
        permisoAcceso = "Acceso permitido";
    }
    else
    {
        permisoAcceso = "Acesso denegado";
    }
    cout << "\nUsted señor: " << nombre
        << "\nEdad: " << edad
        << "\nCarnet: " << Verificacion
        << "\nPermiso especial: " << permisoEspecia
        << "\nResultado: " << permisoAcceso << endl;
}
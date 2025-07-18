#include <iostream>
using namespace std;

int main(){
    int edad;
    cout << "¿Cuántos años tienes? ";
    cin >> edad;

    if (edad <= 17) {
        cout << "Eres menor de edad.";
    }

    return 0;
}

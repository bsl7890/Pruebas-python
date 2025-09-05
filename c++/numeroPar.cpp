#include <iostream>
using namespace std;

int main(){
    for (int i = 1; i <=10; i++)
    {
        if (i % 2 == 0)
        {
            cout << "El numero: " << i << " Es par " << endl;
        }
        else
        {
            cout << "El numero: " << i << " Es impar " << endl;
        }
    }
    return 0;
}
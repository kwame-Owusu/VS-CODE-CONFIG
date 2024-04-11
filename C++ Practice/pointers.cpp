#include <iostream>
using namespace std;



int main() {
  string name = "Kwame";
  string *pName = &name;
  string free_pizzas[5] = {"pizza1","pizza2","pizza3","pizza4","pizza5"};
  // string *pFree_pizzas = &free_pizzas;
  for(auto item: free_pizzas){
    cout<<item<<" "<<endl;
  }

  cout<< *pName<<endl;
  cout<<free_pizzas<<endl;

  return 0;
}



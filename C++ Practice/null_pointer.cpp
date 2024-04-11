#include <iostream>
using namespace std;




int main(){
  int *pointer= nullptr;
  int x  = 123;
  pointer = &x;
  
  if (pointer == nullptr)
  {
    cout<<"address not assigned";
    
  }
  else{
    cout <<"address was assigned"<<endl;
    cout<<*pointer<<endl;
  }


  
  
  return 0;
}
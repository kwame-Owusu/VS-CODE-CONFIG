#include <iostream>


int factorial(int num) {
  if (num == 1)
    return 1;
  else{
    return num * factorial( num - 1);
  }
}


int main() {
  long long num_input;
  std::cout <<"Enter a number" <<std::endl;
  std::cin >>num_input;
  int result = factorial(num_input);
  std::cout << result <<std::endl;
  return 0;
}
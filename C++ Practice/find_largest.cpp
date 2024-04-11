#include <iostream>
using std::cout, std::string, std::cout, std::endl, std::cin;
// given an array of five integers, return the biggest number
// example: [13,07,19,29,23]

// this is BIG O(n) because it is going to iterate thorugh the whole array to find answer
// which means it runs in linear time.


int find_largest(int array[], int size) {
  int i;
  int largest = array[0];
  
  for (i = 0; i < size; i++){
    if (array[i] > largest){
      largest = array[i];
    }
  }
  return largest;

}



int main() {
  int array[] = {13,07,19,29,23, 90, 2000, 91} ;
  int size = sizeof(array) / sizeof(array[0]);
  int result  = find_largest(array, size);
  cout <<"Largest number in array is " << result ;
  return 0;
}
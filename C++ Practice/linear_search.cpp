#include <iostream>

int LinearSearch(int *array, int size, int target);

int LinearSearch(int *array, int size, int target){
  for (int i = 0; i < size; i++ ) 
    if (array[i] == target) 
      return i;
    
  return -1;
  

}



int main () {
  // settings parameters for the function
  int arr[] = {1,4,5,6,7};
  int length =  sizeof(arr) / sizeof(arr[0]);
  int target = 7;
  
  //function call
  int result = LinearSearch(arr, length, target);
  if (result == -1) {
    std::cout<<"Target is not in array" << std::endl;
  }
  else {
    std::cout<<"Target present in array at index " << result;
  }
}

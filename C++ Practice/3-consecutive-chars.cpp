#include <iostream>
#include <sstream>
using std::string, std::cout, std::cin, std::endl;


void find_chars( string word){
 int n = word.length();
 for (int i = 0; i < n; i++) {
  if (word[i] == word[i+1] && word[i] == word[i+2]) {
    cout << word[i];
  }
 }
 
}


int main(){
 string word = "youtttube";
 find_chars(word);
 return 0;
}



// void find_chars(string word){
//  cout << word;
// }
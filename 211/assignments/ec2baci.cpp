#include <iostream>
using namespace std;
void printTwo(int y[], int size) {
  for(int i = 0; i < size; i++){
    if(i % 2 == 0) {
      cout << y[i] << " ";
      y[i] += 2;
    } else {
      y[i] *= 2;
    }
  }
   
}

 

int main() {
  int n = 5;
  int x[5] = {3,4,5,6,7};
  printTwo(x, n);
  return 0;
}


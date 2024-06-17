// Write a program to find and print the first perfect square (i*i) whose last
// two digits are both odd.
#include <iostream>
using namespace std;
int main() {
  int i = 0;
  int square = 0;
  while (true) {
    square = i * i;
    //if square is max int size, break
    if (square < 0) {
        cout << "No perfect square found less than 2147483647" << endl;
      break;
    }
    if (square % 100 / 10 % 2 == 1 && square % 10 % 2 == 1) {
      cout << square << endl;
      break;
    }
    i++;
  }
}
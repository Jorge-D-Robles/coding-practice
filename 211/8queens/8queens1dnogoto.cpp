/*
@author: Jorge Robles
@version 3.0: 01/12/2023
@description: 8 queens problem using a single array without goto
*/
#include <cmath>
#include <iostream>
using namespace std;
void print(int q[], int sol) { cout << "Solution # " << sol << endl; }
bool ok() { return true; }

int main() {
  int q[8], c = 0, solutions = 0;
  q[0] = 0;
  // next column backtracking point, using a permanent loop that breaks at c =
  // -1
  while (true) {
    c++;
    if (c == 8) {
      print(q, ++solutions);
      c--;
      continue;
    }
    // if (c == -1) return 0;
    while (true) {
      q[c]++;
      if (q[c] == 8) c--;
      if (c == -1) return 0;
    }
  }

  return 0;
}

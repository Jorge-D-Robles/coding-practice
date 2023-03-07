/*
@author: Jorge Robles
@version 2.0: 01/09/2023
@description: 8 queens problem using a single array
*/
#include <cmath>
#include <iostream>
using namespace std;
int main() {
  int q[8], c = 0, solutions = 0;
  q[0] = 0;
  // next column backtracking point
nc:
  c++;
  if (c == 8) goto print;
  q[c] = -1;
// next row backtracking point
nr:
  q[c]++;
  if (q[c] == 8) goto backtrack;

  /*MOVING QUEEN FORWARD, ONE TEST*/
  // if row test or diag test
  for (int i = 0; i < c; i++) {
    if ((q[i] == q[c]) or (abs((q[c] - q[i])) == (c - i))) goto nr;
  }
  goto nc;
backtrack:  // backtrack to the previous column
  c--;
  if (c == -1) return 0;
  goto nr;
print:
  solutions++;
  cout << "Solution #" << solutions << ":\n";
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      if (q[i] == j)
        cout << "1 ";
      else
        cout << "0 ";
    }
    cout << endl;
  }
  cout << endl;
  goto backtrack;

  return 0;
}

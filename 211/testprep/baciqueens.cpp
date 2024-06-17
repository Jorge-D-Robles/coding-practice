/*
@author: Jorge Robles, Nikola Baci
@version 3.0: 01/12/2023
@description: 8 queens problem using a single array without goto
partial source code generously shared by Nikola Baci during 1/12/23 class
*/
#include <cmath>
#include <iostream>
using namespace std;
void print(int q[], int sol) {
  cout << "Solution #" << sol << ":\n";
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      if (q[i] == j)
        cout << "1 ";
      else
        cout << "0 ";
    }
    cout << endl;
  }
}
bool ok(int q[], int c) {
  for (int i = 0; i < c; i++) {
    if (q[c] == q[i] or abs(q[c] - q[i]) == c - i) return false;
  }
  return true;
}

int main() {
  int q[8] = {0}, c = 0, solutions = 0;
  q[0] = 0;
  // next column backtracking point, using a permanent loop that breaks at c =
  // -1
  while (true) {
    c++;           // once a valid position is found, go to the next column
    if (c == 8) {  // once all 8 positions are set, then print the solution
      print(q, ++solutions);
      c--;  // backtrack to the previous column, and try the next row
    } else {
      q[c] = -1;  // reset the current row in the column
    }

    while (true) {  // this inner loop does all the backtracking
      q[c]++;       // this goes to the next row in the same column
      if (q[c] == 8) {
        c--;  // this goes back to the previous column
        if (c == -1) {
          return 0;  // when done with all solutions
        }
      } else if (ok(q, c)) {  // once a valid position is found, go to the next
                              // column
        break;
      }
    }
  }
  return 0;
}

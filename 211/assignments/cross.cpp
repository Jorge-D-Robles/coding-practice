/*
@author: Jorge Robles
@version 1.0: 01/12/2023
@description: 8 numbers in a cross using a single array without goto
Partial code from main used with permission written by Nikola Baci during
1/12/23 class
*/
#include <cmath>
#include <iostream>
using namespace std;
void print(int q[], int sol) {
  cout << "Solution #" << sol << ":\n";
  cout << "  " << q[1] << " " << q[4] << endl;
  cout << q[0] << " " << q[2] << " " << q[5] << " " << q[7] << endl;
  cout << "  " << q[3] << " " << q[6] << endl;
}

bool ok(int q[], int c) {
  /*
  using cross counting vertically downwards left->right:
    1 4
  0 2 5 7
    3 6
  */
  static int neighbor[8][5] = {{-1},              // 0
                               {0, -1},           // 1
                               {0, 1, -1},        // 2
                               {0, 2, -1},        // 3
                               {1, 2, -1},        // 4
                               {1, 2, 3, 4, -1},  // 5
                               {2, 3, 5, -1},     // 6
                               {4, 5, 6, -1}};    // 7
  for (int i = 0; i < c; i++)
    if (q[c] == q[i]) return false;  // if same number used already, false
  for (int i = 0; neighbor[c][i] != -1; i++) {
    if (abs(q[c] - q[neighbor[c][i]]) == 1)
      return false;  // if difference is 1 between current square and it's
                     // neighbors, not valid
  }
  return true;
}

int main() {
  int q[8] = {0}, c = 0, solutions = 0;
  q[0] = 0;
  // next column backtracking point, using a permanent loop that breaks at c =
  // -1
  while (true) {
    c++;
    if (c == 8) {
      print(q, ++solutions);
      c--;
    } else {
      q[c] = -1;
    }

    while (true) {
      q[c]++;
      if (q[c] == 8) {
        c--;
        if (c == -1) {
          return 0;
        }
      } else if (ok(q, c)) {
        break;
      }
    }
  }
  return 0;
}

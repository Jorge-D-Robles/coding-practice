/*
@author: Jorge Robles
@version 1.0: 01/12/2023
@description: stable marriage
partial source code generously shared by Nikola Baci during 1/12/23 class
*/
#include <cmath>
#include <iostream>
using namespace std;
void print(int q[], int sol) {
  cout << "Solution #" << sol << ":\n";
  for (int i = 0; i < 3; i++) {
    cout << "Man # " << i << "-> Woman # " << q[i] << endl;
  }
}
bool ok(int q[], int col) {
  /* How to decipher the mp and wp arrays:
  cm = curent man
  cw = current woman
  nm = new man
  nw = new woman, nm and nw are proposed pair
  */
  static int mp[3][3] = {{0, 2, 1}, {0, 2, 1}, {1, 2, 0}};
  static int wp[3][3] = {{2, 1, 0}, {0, 1, 2}, {2, 0, 1}};
  int i, cm, cw, nm, nw;
  nm = col;
  nw = q[col];
  for (i = 0; i < col; i++)
    if (q[i] == nw) return false;
  for (cm = 0; cm < col; cm++) {
    cw = q[cm];
    if (mp[cm][cw] > mp[cm][nw] && wp[nw][nm] > wp[nw][cm]) return false;
    if (mp[nm][nw] > mp[nm][cw] && wp[cw][cm] > wp[cw][nm]) return false;
  }
  return true;
}
int main() {
  int q[3] = {0}, c = 0, solutions = 0;
  q[0] = 0;
  // next column backtracking point, using a permanent loop that breaks at c =
  // -1
  while (true) {
    c++;
    if (c == 3) {
      print(q, ++solutions);
      c--;
    } else {
      q[c] = -1;
    }

    while (true) {
      q[c]++;
      if (q[c] == 3) {
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

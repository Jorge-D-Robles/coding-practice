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
bool ok(int q[], int c) {
  /* How to decipher the mp and wp arrays:
  mp[i] is NEW MAN
  mp[c] is CURRENT MAN

  mp[i/c][q[c]] is NEW WOMAN
  mp[i/c][q[i]] is CURRENT WOMAN

  wp[q[c]] is NEW WOMAN
  wp[q[i]] is CURRENT WOMAN

  wp[q[i/c]][c] is NEW MAN
  wp[q[i/c]][i] is CURRENT MAN
  */
  static int mp[3][3] = {{0, 2, 1}, {0, 2, 1}, {1, 2, 0}};
  static int wp[3][3] = {{2, 1, 0}, {0, 1, 2}, {2, 0, 1}};
  for (int i = 0; i < c; i++) {  // for each prior man i,

    if (q[i] == q[c])
      return false;  // if man c and man i are with the same woman

    if ((mp[i][q[i]] > mp[i][q[c]] and
         wp[q[i]][i] > wp[q[i]][c]) or  // new man prefers current woman to his
                                        // partner, and current woman prefers
                                        // new man to her partner
        (mp[c][q[c]] > mp[c][q[i]] and
         wp[q[c]][c] >
             wp[q[c]][i]))  // current man prefers new woman to his partner, and
                            // new woman prefers current man to her partner

      return false;
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

/*
@author: Jorge Robles
@version 1.0: 01/12/2023
@description: 8 queens problem, the dumb way using 8 for loops
reused print function from prior 8queens, minor adjustments to ok function in
order to work with 8 for loops
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
bool ok(int q[]) {
  // tests row, up diag, down diag
  for (int c = 0; c < 8; c++) {
    for (int i = 0; i < c; i++) {
      if (q[c] == q[i] or (c - i == abs(q[c] - q[i]))) return false;
    }
  }
  return true;
}

int main() {
  int q[8] = {0}, solutions = 0;
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      for (int k = 0; k < 8; k++) {
        for (int l = 0; l < 8; l++) {
          for (int m = 0; m < 8; m++) {
            for (int n = 0; n < 8; n++) {
              for (int o = 0; o < 8; o++) {
                for (int p = 0; p < 8; p++) {
                  q[0] = i;
                  q[1] = j;
                  q[2] = k;
                  q[3] = l;
                  q[4] = m;
                  q[5] = n;
                  q[6] = o;
                  q[7] = p;
                  if (ok(q)) print(q, ++solutions);

                  /* try literally every single permuation of where a queen can
                  possibly be if it's valid, print it. THIS IS VERY BAD */
                }
              }
            }
          }
        }
      }
    }
  }
  return 0;
}

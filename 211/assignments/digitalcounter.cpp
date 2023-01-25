#include <iostream>
using namespace std;
int main() {
  // digital odometer, 6 windows with miles starting 000000 ending 999999 using
  // for loops. create a 1d array of size 6, where each element is one window of
  // the odometer. win[0] is the left and win[5] is the right.
  int win[6];
  // initialize the odometer to 000000
  for (int i = 0; i < 6; i++) {
    win[i] = 0;
  }
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      for (int k = 0; k < 10; k++) {
        for (int l = 0; l < 10; l++) {
          for (int m = 0; m < 10; m++) {
            for (int n = 0; n < 10; n++) {
              for (int o = 0; o < 10; o++) {
                win[0] = i;
                win[1] = j;
                win[2] = k;
                win[3] = l;
                win[4] = m;
                win[5] = n;
                win[6] = o;
              }
              for (int i = 0; i < 6; i++) {
                cout << win[i];
              }
              cout << endl;
            }
          }
        }
      }
    }
  }
}
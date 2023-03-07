/*
@author: Jorge Robles
@version 1.0: 01/ 05/2022
@description: 8 queens problem using backtracking
*/
#include <iostream>
using namespace std;
int main() {
  // create a 2d array of size 8x8
  // initialize the array to 0
  int b[8][8] = {0}, row, col = 0;
  // place a queen in the first row, first column
  b[0][0] = 1;
// next column backtracking point
nc:
  col++;
  if (col == 8) goto print;
  row = -1;

// next row backtracking point
nr:
  row++;
  if (row == 8) goto backtrack;
  // check if the queen is in a safe position

  /*MOVING QUEEN FORWARD, ALL TESTS*/

  // rowTest
  for (int i = 0; i < col; i++) {
    if (b[row][i] == 1) goto nr;
  }
  // up Diagonal Test
  for (int i = 1; (row - i) >= 0 and (col - i) >= 0; i++) {
    if (b[row - i][col - i] == 1) goto nr;
  }
  // down Diagonal Test
  for (int i = 1; (row + i) < 8 and (col - i) >= 0; i++) {
    if (b[row + i][col - i] == 1) goto nr;
  }

  /* END TESTS*/

  // if it is safe, place a queen in the current position
  b[row][col] = 1;
  // move to the next column
  goto nc;

backtrack:  // backtrack to the previous column
  col--;
  if (col == -1) return 0;
  // find the row with a queen in it
  row = 0;
  while (b[row][col] != 1) row++;
  b[row][col] = 0;
  goto nr;

print:
  /* Have to use static int to keep the value of solutions between calls
  to print because goto does not preserve local variables */
  static int solutions = 0;
  cout << "Solution #" << ++solutions << ":\n";
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      cout << b[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
  goto backtrack;

  return 0;
}

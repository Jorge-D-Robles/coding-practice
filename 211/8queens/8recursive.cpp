#include <iostream>

using namespace std;

const int N = 8;  // size of the chessboard
int queens[N];    // positions of the queens on the chessboard

// check if it is safe to place a queen at (row, col)
bool isSafe(int row, int col) {
  for (int i = 0; i < row; i++) {
    // check if there is a queen in the same column
    if (queens[i] == col) {
      return false;
    }
    // check if there is a queen on the diagonal
    if (abs(queens[i] - col) == abs(i - row)) {
      return false;
    }
  }
  return true;
}

// recursive function to solve the 8 queens problem
bool solve(int row) {
  // base case: if all queens are placed, return true
  if (row == N) {
    return true;
  }

  for (int col = 0; col < N; col++) {
    // check if it is safe to place a queen at (row, col)
    if (isSafe(row, col)) {
      // place the queen and move on to the next row
      queens[row] = col;
      if (solve(row + 1)) {
        return true;
      }
      // backtrack and try a different position
      queens[row] = -1;
    }
  }

  return false;
}

int main() {
  // initialize the chessboard
  for (int i = 0; i < N; i++) {
    queens[i] = -1;
  }

  if (solve(0)) {
    // print the positions of the queens
    for (int i = 0; i < N; i++) {
      cout << queens[i] << " ";
    }
    cout << endl;
  } else {
    cout << "No solution found" << endl;
  }

  return 0;
}
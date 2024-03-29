#include <cmath>
#include <iostream>
using namespace std;

// Returns true if the number written in square c is ok.
bool ok(int q[], int c) {
  static int adj[8][5] = {{-1},        // 0  Neighbor list for each square
                          {0, -1},     // 1
                          {0, 1, -1},  // 2  The cross with the squares labeled:
                          {0, 2, -1},  // 3                  1 4
                          {1, 2, -1},  // 4                0 2 5 7
                          {1, 2, 3, 4, -1},  // 5            3 6
                          {2, 3, 5, -1},     // 6
                          {4, 5, 6, -1}};    // 7

  for (int i = 0; i < c; ++i)
    // If the number in square c has already been used, return false.
    if (q[i] == q[c]) return false;

  for (int i = 0; adj[c][i] != -1; ++i)  // For each neighbor of square c,
    if (abs(q[c] - q[adj[c][i]]) ==
        1)  // if the numbers written in square c and the neighbor differ by 1,
            // return false.
      return false;
  return true;
}

void print(int q[]) {
  static int solution = 0;
  cout << "Solution #" << ++solution << "\n";
  cout << " " << q[1] << q[4] << "\n";
  cout << q[0] << q[2] << q[5] << q[7] << "\n";
  cout << " " << q[3] << q[6] << "\n\n";
}

void next(int q[], int c) {
  if (c == 8)
    print(q);
  else
    for (q[c] = 1; q[c] <= 8; ++q[c])
      if (ok(q, c)) next(q, c + 1);
}

int main() {
  int q[8];
  next(q, 0);
  return 0;
}
#include <iostream>
using namespace std;
int weirdFunction(int x) {
  if (x < 10) return x;
  if (x % 10 == 0) return weirdFunction(x / 10);
  return x % 10 + 10 * weirdFunction(x / 10);
}

int main() {
  int n = 109203;
  cout << weirdFunction(n);
}

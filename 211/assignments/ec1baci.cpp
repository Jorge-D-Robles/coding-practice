#include <iostream>
using namespace std;
int main() {
  // for each sum, write a function to compute and return the value of the sum.
  // assume the value of n is an argument of the function the sum s = 1 - 1/2 +
  // 1/3 - 1/4 + .... (+/-) 1/n

  int n;
  double sum = 0;
  cout << "Enter a number: ";
  cin >> n;
  for (int i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      sum -= 1.0 / i;
    } else {
      sum += 1.0 / i;
    }
  }
  cout << "The sum of the first " << n << " numbers is " << sum << endl;
  return 0;
}
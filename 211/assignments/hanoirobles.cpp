#include <iostream>
#include <vector>
using namespace std;
int main() {
  vector<int> t[3];
  int n;
  cout << "Enter the number of disks: ";
  cin >> n;
  cout << endl;
  // if n is odd, close is 1, far is 2. Else, close is 2, far is 1.
  int close = (n % 2 == 0 ? 2 : 1), far = (n % 2 == 0 ? 1 : 2);
  int from = 0, to = close, candidate = 1, move = 0;
  // initializing towers
  for (int i = n; i >= 1; i--) {
    t[0].push_back(i);
  }
  t[1].push_back(n + 1);
  t[2].push_back(n + 1);

  // while first tower t[1] does not have every disk
  while (t[1].size() < n + 1) {
    cout << "Move #" << ++move << ": Transfer ring " << candidate
         << " from tower " << char(from + 'A') << " to tower " << char(to + 'A')
         << "\n";

    // Move the ring from the "from" tower to the "to" tower.
    t[to].push_back(t[from].back());
    t[from].pop_back();
    // Determine the "from" tower (the smallest available ring that has not just
    // been moved).
    if (t[(to + 1) % 3].back() < t[(to + 2) % 3].back())

      from = (to + 1) % 3;
    else
      from = (to + 2) % 3;
    candidate = t[from].back();
    // The candidate is the ring on top of the "from" tower.

    if (t[(from + close) % 3].back() > candidate)  // Determine the "to" tower.
      to = (from + close) % 3;
    // (the closest tower on which the ring can be placed)
    else
      to = (from + far) % 3;
  }
}

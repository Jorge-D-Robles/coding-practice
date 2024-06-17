#include <iostream>
#include <vector>
using namespace std;
int main() {
  vector<int> t[3];
  int close, far, candidate = 1, n, move = 0;
  cout << "Enter number of disks: ";
  cin >> n;
  if (n % 2 == 0) {
    close = 2;
    far = 1;
  } else {
    close = 1;
    far = 2;
  }
  int from = 0, to = close;
  for (int i = n + 1; i >= 1; --i) t[0].push_back(i);
  t[1].push_back(n + 1);
  t[2].push_back(n + 1);
  while (t[1].size() < n + 1) {
    cout << "Move disk " << t[from].back() << " from tower " << from + 1
         << " to tower " << to + 1 << endl;
    t[to].push_back(t[from].back());
    t[from].pop_back();
    move++;
    if (t[(to + 1) % 3].back() < t[(to + 2) % 3].back()) {
      from = (to + 1) % 3;
      to = (to + 2) % 3;
    } else {
      from = (to + 2) % 3;
      to = (to + 1) % 3;
    }
  }

  cout << "Total moves: " << move << endl;
}

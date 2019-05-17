#include <iostream>
using namespace std;
int main() {
  long int a, b, total;
  cin >> a;
  cin >> b;
  total = a;
  for (long int i = a+1; i < b+1; i++) {
    total = total ^ i;
  }
  cout << total << endl;
  return 0;
}

#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<functional>
#include <numeric>
using namespace std;

bool comp(pair<int, int> &a, pair<int, int> &b){
  return (a.second - a.first) < (b.second - b.first);
}

int solver() {
  int n, q;
  vector<pair<int, int> > bookings;
  cin >> n >> q;
  int seats[n+1];
  for (int i = 0; i < n+1; i++) {
    seats[i] = 0;
  }
  int min = n;
  for (int i = 0; i < q; i++) {
    int start, end;
    cin >> start >> end;
    bookings.push_back({start, end});
  }
  //sort(bookings.begin(), bookings.end(), comp);
  int factorial = 1;
  for(int i = 1; i <=q; ++i)
  {
    factorial *= i;
  }
  int totalmin = 0;
  const int N = q;
  vector<int> v(N);
  std::iota(v.begin(), v.end(), 0);       // v に 1, 2, ... N を設定
  //for (int i = 0; i < q; i++) {
  //std::cout << bookings[i].first << '\n';
  //}

  for (int k = 0; k < factorial; k ++){
    for (int l = 0; l < q; l++) {
      std::cout << "v" << v[l] << '\n';
    }
    for (int i = 0; i < q; i++) {
      int count = 0;
      std::cout << "min" <<min << '\n';
      for (int j = bookings[v[i]].first; j < bookings[v[i]].second+1; j++) {
        std::cout << "books" << j << '\n';
        std::cout << "emp" << seats[j] << '\n';
        if (seats[j] == 0) {
          seats[j] = 1;
          count++;
          //cout << "seats" << j << '\n';
        }
      }
      if (count < min) {
        min = count;
      }

    }
    if (k ==0) {
      totalmin = min;
    }

    if (min > totalmin) {
      totalmin = min;
    }

    std::cout << "totalmin" << totalmin << '\n';
    next_permutation(v.begin(), v.end());
  }
  return totalmin;
}

int main() {
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; i++) {
    cout << "Case #" << i+1 << ": " << solver() << '\n';
  }
  return 0;
}

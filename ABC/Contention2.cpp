#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<functional>
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
  sort(bookings.begin(), bookings.end(), comp);

  //for (int i = 0; i < q; i++) {
    //std::cout << bookings[i].first << '\n';
  //}
  for (int i = 0; i < q; i++) {
    int count = 0;
    //std::cout << "min" <<min << '\n';
    for (int j = bookings[i].first; j < bookings[i].second+1; j++) {
      //std::cout << "books" << j << '\n';
      //std::cout << "emp" << seats[j] << '\n';
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
  return min;
}

int main() {
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; i++) {
    cout << "Case #" << i+1 << ": " << solver() << '\n';;
  }
  return 0;
}

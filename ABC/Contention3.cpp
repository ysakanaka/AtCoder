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
  std::vector<int> book;
  cin >> n >> q;
  int seats[n+1];
  for (int i = 0; i < n+1; i++) {
    seats[i] = 40000;
  }
  int min = n;
  for (int i = 0; i < q; i++) {
    int start, end;
    cin >> start >> end;
    bookings.push_back({start, end});
    book.push_back(0);
  }
  sort(bookings.begin(), bookings.end(), comp);

  for (int t = 0; t < n; t++){
  for (int i = 0; i < q; i++) {
    int count = 0;

    for (int j = bookings[i].first; j < bookings[i].second+1; j++) {
      if (seats[j] == 40000) {
        seats[j] = i;
        count++;
        //cout << "seats" << j << '\n';
      }
      else {
        //std::cout << "seats trade?" << j << '\n';
        if (count < t) {
          book[seats[j]] -= 1;
          seats[j] = i;
          count++;
          //std::cout << "seats traded" << j << '\n';
        }
      }
    }
    book[i] = count;

    if (count == 0) {
      return 0;
    }
  }
  int solution = *std::min_element(book.begin(), book.end());
  if (solution < t) {
    return t;
  }
}

}

int main() {
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; i++) {
    cout << "Case #" << i+1 << ": " << solver() << '\n';;
  }
  return 0;
}

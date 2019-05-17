#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int main() {
  string S;
  cin >> S;

  string T = "ATCG";

  int ans = 0; //ATCG文字列の最大長
  int now = 0; //今見ている文字を末尾とするATCG文字列の最大長
  for (int i = 0; i < count; i++) {
    bool isATCG = false;
    for (int j = 0; j < count; j++) {
      if (S[i] == T[j]) {
        isATCG = true;
      }
    }

    if (!isATCG) {
      //違う場合は0にする
      now = 0;
    } else {
      //ATCG文字の場合は前の文字列に1つ文字を足せる
      now++;
      //最大値を更新する
      ans = max(now, ans);
    }
  }
  std::cout << ans << '\n';
}

class Solution {
public:
    bool isPalindrome(long long x) {
        if (x < 0) return false;
        long long rev = 0, dig, num = x;
        while (num != 0) {
            dig = num % 10;
            rev = rev * 10 + dig;
            num /= 10;
        }
        if (rev == x) return true;
        else return false;
    }
};

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


----

Notes:

- the search for all palindromes for 3 digit numbers starts to get slow
- could make this faster by ...
    - on the inner loop ... the first time we find a palindrome ... that inner loop value (the second smaller factor) ...
    - should define the minimum for the next iteration of the inner loop
    - eg. 999*91 is the first palindrome ... and so when we try 998, we shouldn't iterate past 91
    - though this won't save that much time

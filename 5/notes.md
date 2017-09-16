
# prime factors of 10...1
# 10 = 5 * 2
#  9 = 3
#  8 = 2
#  7 = 7
#  6 = 3 * 2
#  5 = 5
#  4 = 2
#  3 = 3
#  2 = 2

then I think I'd basically walk in the biggest iteration I could?

well the non redundant prime factors are:

2,3,5,7

which doesn't yield 2520


but counting up the factors ...

2,2,2,2,2,2,2,2
3,3,3,3
5,5
7

prod of all those:

2^8
3^4
5^2
7

256
81
25
7

no ... thats way too big

but we can walk by the biggest prime factor ...
then the next biggest one

so increment by 7s

check if div by 5

etc


(even divis == div by each, not div by all ... ok makes this simpler)

---


ok 2520

is div by 7 and 5

biggest prime factors

>>> 2520.0 / (7.0 * 5.0 * 3.0 * 2.0)
12.0


so we can step by the product of the prime factors
or 210.0 in this case

2520 / 210 = 12

which is 3*2*2

and looking at the factors of 10 again ...

# 10 = 5 * 2
#  9 = 3
#  8 = 2
#  7 = 7
#  6 = 3 * 2
#  5 = 5
#  4 = 2
#  3 = 3
#  2 = 2


but counting the prime factors that are needed:

2: 1 for '2', another for '4', another for '8' = 3 total
3: 1 for '3', another for '9' = 2 total
5: 1 for '5', that one will work for '10' as well = 1
7: 1 for '7'

and looking at the prod of all prime factors we get ...

2*3*5*7

so the remaining factor we need to account for is ...

2 2's
1 3

and that exactly makes 12


so ....


if we have the prime factorization of all the numbers ... I think we can get a closed form soln for the answer ... no need to loop to find it




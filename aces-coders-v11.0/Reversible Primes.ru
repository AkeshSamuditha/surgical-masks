# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/reversibleprimes/problem
# Achived a score of 64.3 out of 100 which was good enough for 1st place.
require'prime';(1..1e3).each{|x|x.prime?&&(r=x.digits.join.to_i).prime?&&x!=r&&p(x)}
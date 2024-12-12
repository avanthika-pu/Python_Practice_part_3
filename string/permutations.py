#Python | Permutation of a given string using inbuilt function
import itertools
input_str = "ABC"
permutation_str = itertools.permutations(input_str)
for p in permutation_str:
    print(''.join(p))
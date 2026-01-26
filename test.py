import itertools
import string

key_length = 3
alphabet = string.ascii_uppercase

# for key_index in range(key_length):
#     for alphabet_index in range(alphabet_length):
#         print(key_index,alphabet_index)

possible_keys = []
for i in range(key_length):
    possible_keys += itertools.combinations_with_replacement(alphabet, key_length)



print(possible_keys)
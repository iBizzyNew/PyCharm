import operator
from collections import OrderedDict

my_dict = {'a': 50, 'c': 5, 'd': 56, 'e': 4, 'f': 58, 'z': 20}
sorted_tuples = sorted(my_dict.items(), key=operator.itemgetter(0))
sorted_dict = OrderedDict()
for key, v in sorted_tuples:
    sorted_dict[key] = v
print(sorted_dict)
print(list(sorted_dict.items())[:3])
print(list(sorted_dict.values())[:3])



list = []

set_1 = set()
item_in_set_1 = 'p'

set_2 = set()
item_in_set_2 = 'L'

set_1.add(item_in_set_1)
list.append(set_1)

set_2.add(item_in_set_2)
list.append(set_2)

print(list)



dir_dict = {'a': {'b': {'c': 'foo'}}}
keys = ['a', 'b', 'c']
new_value = int('123')

d = dir_dict
for key in keys[:-1]:
    d = d.get(key)
d[keys[-1]] = new_value

print(d)  # prints {'a': {'b': {'c': 'bar'}}}
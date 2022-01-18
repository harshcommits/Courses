from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
from typing import DefaultDict

a = "aabbbccccc"
my_counter = Counter(a)

print(my_counter)
print(my_counter.values())
print(my_counter.most_common(1))
print(list(my_counter.elements()))

#namedtuple

Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

#ordereddict not valid since functions already available in normal dictionary
#prints data in exact order entered
ordered_dict = OrderedDict()
ordered_dict[1] = 'a'
ordered_dict[2] = 'd'
ordered_dict[3] = 'c'
ordered_dict[4] = 'ab'

print(ordered_dict)

#defaultdict has default key value
#d = defaultdict(int)
d = defaultdict(list)
d[1] = 'a'
d[2] = 'b'
print(d[3])

#deque (double ended queue)
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.popleft()
print(d)

d.extendleft([4,5,6])
print(d)

d.rotate(1)
print(d)
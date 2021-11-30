import matplotlib.pyplot as plt
import collections

#x1 = ['prep1', 'prep2', 'prep3', 'prep4', 'prep5', 'prep6', 'prep7']
#x2 = ['751', '752', '753', '754', '755', '756']

slow = collections.defaultdict(list)

with open('students.txt') as f:
    for line in f:
        data = line.split(';')
        new = data[2].replace('\n', '')
        slow[data[0]].append(int(new))
print(slow.items())

for key in slow:
    a = [0] * 11
    for i in range(11):
        a[i] = slow[key].count(i)
    slow[key] = a
print(slow.items())

w = 0.5
fig, ax = plt.subplots()
for i in range(1, 11):
    now = [slow[key][i] for key in slow]
    old = [sum(slow[key][j] for j in range(i)) for key in slow]
    ax.bar(list(slow.keys()), now, w, bottom=old, label='%d' % i)

plt.legend()
plt.savefig('001.png')
plt.show()

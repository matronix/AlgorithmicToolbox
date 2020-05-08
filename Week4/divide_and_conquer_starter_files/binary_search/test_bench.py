import random

with open('testdata', 'a') as f:

    for i in range(1000):
        f.write('{}\n'.format(random.randrange(100)))

f.closed

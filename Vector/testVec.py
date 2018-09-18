import random
import vector as v
f = open("input.txt", 'w')
for i in range(100):
    a = random.randint(-10, 10)
    b = random.randint(-15, 18)
    c = random.randint(-20, 20)
    out = ','.join(map(str, (a, b, c))) + '\n'
    f.write(out)
f.close()
print('success')

fr = open("input.txt", 'r')
fo = open("output.txt", 'w')
for line in fr:
    line = line.strip()
    cords = line.split(',')
    cords = tuple(map(int, cords))
    vec = v.Vector(*cords)
    out = vec.__str__() + '\n'
    fo.write(out)

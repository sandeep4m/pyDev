fin = open('students.txt', 'r')
fout = open('output.txt', 'w')


def sumMarks(info):
    Sum = 0
    for i in range(2, 7):
        Sum += int(info[i])
    return(Sum)


math = []
phy = []
chem = []
eco = []
ast = []
Totals = dict()
for line in fin:
    line = line.strip()
    if not line.startswith('-'):
        info = line.split()
        if info[0] == "S.No":
            continue
        total = sumMarks(info)
        name = info[1]
        Id = info[0]
        Totals[(total, Id)] = name
        if int(info[2]) >= 98:
            math.append(name)
        if int(info[3]) >= 98:
            phy.append(name)
        if int(info[4]) >= 98:
            chem.append(name)
        if int(info[5]) >= 98:
            eco.append(name)
        if int(info[6]) >= 98:
            ast.append(name)

fout.write("Maths:" + ",".join(math) + '\n')
fout.write("Physics:" + ",".join(phy) + '\n')
fout.write("Chemistry:" + ",".join(chem) + '\n')
fout.write("Economics:" + ",".join(eco) + '\n')
fout.write("Astronomy:" + ",".join(ast) + '\n')

marks = list(Totals.keys())
marks.sort(reverse=True)
first = [marks[0][1], Totals[marks[0]], str(marks[0][0])]
second = [marks[1][1], Totals[marks[1]], str(marks[1][0])]
third = [marks[2][1], Totals[marks[2]], str(marks[2][0])]
fout.write(" ".join(first) + '\n')
fout.write(" ".join(second) + '\n')
fout.write(" ".join(third) + '\n')
fin.close()
fout.close()

import random as R

letters = []
for i in range(97, 123):
    letters.append(chr(i))


def markGen():
    return(str(R.randrange(20, 101)))


f = open("students.txt", "w")
headings = ["{0:10}".format("Name"), "Maths", "Physics", "Chemistry", "Economics", "Astronomy"]
f.write("{0:6}".format("S.No") + " ".join(headings) + '\n')
f.write(61 * "-" + "\n")

for i in range(1210):
    nameLength = R.randrange(4, 11)
    name = ""
    for j in range(nameLength):
        name = name + R.choice(letters)
    name = name.capitalize()
    marks = []
    for sub in range(5):
        if sub == 0:
            marks.append("{0:5}".format(markGen()))
        elif sub == 1:
            marks.append("{0:7}".format(markGen()))
        elif sub == 2:
            marks.append("{0:9}".format(markGen()))
        elif sub == 3:
            marks.append("{0:9}".format(markGen()))
        elif sub == 4:
            marks.append("{0:9}".format(markGen()))
    marksStr = " ".join(marks)
    line = "{0:6}".format(str(i) + ")") + "{0:10}".format(name) + " " + marksStr
    f.write(line + '\n')

f.close()

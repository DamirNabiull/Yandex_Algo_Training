import sys
a, b, c, d, e, f = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())

matrix, answers = [], []

if a != 0:
    matrix = [
        [a, b],
        [c * a - a * c, d * a - b * c]
    ]
    answers = [e, f * a - e * c]
else:
    matrix = [
        [c, d],
        [a, b]
    ]
    answers = [f, e]

for i in range(2):
    if (matrix[i][0] == 0) and (matrix[i][1] == 0) and (answers[i] != 0):
        print(0)
        sys.exit()

if (matrix[1][1] == 0) and (answers[1] == 0) and (matrix[0][0] != 0) and (matrix[0][1] != 0):
    print(1, -matrix[0][0]/matrix[0][1], answers[0]/matrix[0][1])
    sys.exit()
elif (matrix[1][1] != 0) and (matrix[0][0] != 0):
    y = answers[1]/matrix[1][1]
    x = (answers[0] - (y*matrix[0][1]))/matrix[0][0]
    print(2, x, y)
    sys.exit()
elif (matrix[0][0] != 0) and (matrix[0][1] == 0) and (matrix[1][1] == 0) and (answers[1] == 0):
    x = answers[0]/matrix[0][0]
    print(3, x)
    sys.exit()
elif (matrix[0][0] == 0):
    if (matrix[0][1] != 0) and (matrix[1][1] != 0):
        answers[1] = answers[1] * matrix[0][1] - (answers[0] * matrix[1][1])
        matrix[1][1] = matrix[1][1]*matrix[0][1] - matrix[1][1]*matrix[0][1]
        if (matrix[1][1] == 0) and (answers[1] == 0):
            y = answers[0]/matrix[0][1]
            print(4, y)
            sys.exit()
        else:
            print(0)
            sys.exit()
    elif (matrix[0][1] != 0) and (matrix[1][1] == 0):
        if (matrix[1][1] == 0) and (answers[1] == 0):
            y = answers[0]/matrix[0][1]
            print(4, y)
            sys.exit()
        else:
            print(0)
            sys.exit()
    elif (matrix[0][1] == 0) and (matrix[1][1] != 0):
        if (matrix[0][1] == 0) and (answers[0] == 0):
            y = answers[1]/matrix[1][1]
            print(4, y)
            sys.exit()
        else:
            print(0)
            sys.exit()
print(5)

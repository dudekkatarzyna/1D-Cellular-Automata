def toBinary(n):
    binArr = []
    bin = '{:08b}'.format(n)
    for i in range(len(bin)):
        if int(bin[i]):
            binArr.append(True)
        else:
            binArr.append(False)

    return binArr


def countValue(regula, a, b, c):
    if a and b and c:
        return regula[0]

    elif a and b and not c:
        return regula[1]

    elif a and not b and c:
        return regula[2]

    elif a and not b and not c:
        return regula[3]

    elif not a and b and c:
        return regula[4]

    elif not a and b and not c:
        return regula[5]

    elif not a and not b and c:
        return regula[6]

    elif not a and not b and not c:
        return regula[7]


def calculate(self, surface, size, regula):
    regulaBin = toBinary(regula)

    for line in range(1, size - 1):

        for i in range(size):

            if i == 0:

                value = countValue(regulaBin, surface[line - 1][size - 1], surface[line - 1][i],
                                   surface[line - 1][i + 1])
                surface[line][i] = value

            elif i == size - 1:
                value = countValue(regulaBin, surface[line - 1][i - 1], surface[line - 1][i],
                                   surface[line - 1][0])
                surface[line][i] = value

            else:
                value = countValue(regulaBin, surface[line - 1][i - 1], surface[line - 1][i],
                                   surface[line - 1][i + 1])
                surface[line][i] = value

        return surface

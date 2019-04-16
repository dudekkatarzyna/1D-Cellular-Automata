class Algorithm:
    def toBinary(self, n, r2):
        return int(bin(n)[2:])

    def countValue(self, regula, a, b, c):

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

    def calculate(self, surface, size, regula, regulaBin):

        self.toBinary(regula, regulaBin)

        surface[0][size / 3] = True

        for line in range(1, size - 1):

            for i in range(size):

                if i == 0:

                    value = self.countValue(regulaBin, surface[line - 1][size - 1], surface[line - 1][i],
                                            surface[line - 1][i + 1])
                    surface[line][i] = value

                elif i == size - 1:
                    value = self.countValue(regulaBin, surface[line - 1][i - 1], surface[line - 1][i],
                                            surface[line - 1][0])
                    surface[line][i] = value

                else:
                    value = self.countValue(regulaBin, surface[line - 1][i - 1], surface[line - 1][i],
                                            surface[line - 1][i + 1])
                    surface[line][i] = value

            return surface

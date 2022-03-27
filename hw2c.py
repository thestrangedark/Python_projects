def det(m, n):
    if n == 1: return m[0][0]
    z = 0
    for r in range(n):
        k = m[:]
        del k[r]
        z += m[r][0] * (-1) ** r * det([p[1:] for p in k], n - 1)
    return z

def Cramer(Aaug, x):
 w = len(x)  # find length
 d = det(Aaug, w)
 if d == 0:
  r = []
 else:
  r = [det([r[0:i] + [s] + r[i + 1:] for r, s in zip(Aaug, x)], w) / d for i in range(w)] #caluations
 print(r)
 return r

def main():
        MA = [[3, 1, -1, 2],  # augmented matrix
              [1, 4, 1, 12],
              [2, 1, 2, 10]]
        x1 = [0, 0, 0]

        MB = [[1, -10, 2, 4, 2],  # augmented matrix
              [3, 1, 4, 12, 12],
              [9, 2, 3, 4, 21],
              [-1, 2, 7, 3, 37]]
        x2 = [0, 0, 0, 0]

        xsolution1 = Cramer(MA, x1)
        xsolution2 = Cramer(MB, x2)

        print('Solutions', '\nMatrix A=', [round(x, 4) for r in xsolution1], '\nMatrix B=',
              [round(x, 4) for r in xsolution2])  # print results


main()

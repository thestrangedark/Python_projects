
def multimatrix(M, N):
    """Multiply square matrices of same dimension M and N"""

    tuple_N = N

    # Nested list comprehension to calculate matrix multiplication
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]


def Doolittle(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    # Create an identity matrix, with floating point values
    id_mat = [[float(i == j) for i in range(m)] for j in range(m)]

    # Rearrange the identity matrix such that the largest element of
    # each column of M is placed on the diagonal of M
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            # Swap the rows
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat


def LUFactorization(A):
    """Performs an LU Decomposition of A (which must be square)
    into PA = LU. The function returns P, L and U."""
    n = len(A)

    # Create zero matrices for L and U
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    # Create the pivot matrix P and the multipled matrix PA
    P = Doolittle(A)
    PA = multimatrix(P, A)

    # Perform the LU Decomposition
    for j in range(n):
        # All diagonal entries of L are set to unity
        L[j][j] = 1.0

        # LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1

        # LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

    return P, L, U


def main():
    A = [[3, 9, 6, 4.6], [18, 48, 39, 27.2], [9, -27, 42, 9]]  # given matrix
    P, L, U = LUFactorization(A) # some packing
    # print statement
    print('Solutions', '\nMatrix A=', [A], '\nMatrix P=',
          [P], '\nMatrix L=', [L], '\nMatrix U=', [U],)


main()

# followed online tutorial for parts of to help with the coding

import itertools

def is_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def n_queens_bruteforce(n):

    solutions = []
    for permutation in itertools.permutations(range(n)):
        if is_valid(permutation):
            solutions.append(permutation)
    return solutions

print(len(n_queens_bruteforce(int(input()))))


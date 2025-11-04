"""
Backtracking Problems - N-Queens e Sudoku Solver
"""
from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """
    Resolve o problema das N rainhas.
    
    Args:
        n: Tamanho do tabuleiro (n x n)
        
    Returns:
        Lista com todas as soluções possíveis
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_valid(row: int, col: int) -> bool:
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] = 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row: int):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    backtrack(0)
    return result


def solve_sudoku(board: List[List[str]]) -> None:
    """
    Resolve um Sudoku 9x9 usando backtracking.
    Modifica o board in-place.
    
    Args:
        board: Tabuleiro 9x9 com '.' para células vazias
    """
    def is_valid(row: int, col: int, num: str) -> bool:
        for x in range(9):
            if board[row][x] == num:
                return False
        
        for x in range(9):
            if board[x][col] == num:
                return False
        
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True
    
    def solve() -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if is_valid(row, col, num):
                            board[row][col] = num
                            
                            if solve():
                                return True
                            
                            board[row][col] = '.'
                    return False
        return True
    
    solve()


def permute(nums: List[int]) -> List[List[int]]:
    """
    Gera todas as permutações de uma lista de números.
    """
    result = []
    
    def backtrack(current: List[int], remaining: List[int]):
        if not remaining:
            result.append(current[:])
            return
        
        for i in range(len(remaining)):
            backtrack(current + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    backtrack([], nums)
    return result


if __name__ == "__main__":
    print("N-Queens (n=4):")
    queens_result = solve_n_queens(4)
    for idx, solution in enumerate(queens_result):
        print(f"Solução {idx + 1}:")
        for row in solution:
            print(row)
        print()
    
    print("\nSudoku Solver:")
    sudoku_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    solve_sudoku(sudoku_board)
    print("Sudoku resolvido:")
    for row in sudoku_board
        print(' '.join(row))
    
    print("\nPermutations:")
    print(permute([1, 2, 3]))

/**
 * N-Queens Problem
 * Coloca N rainhas em um tabuleiro NxN sem que se ataquem
 * @param {number} n
 * @return {string[][]}
 */
function solveNQueens(n) {
    const result = [];
    const board = Array(n).fill().map(() => Array(n).fill('.'));
    
    function isValid(row, col) {
        for (let i = 0; i < row; i++) {
            if (board[i][col] === 'Q') {
                return false;
            }
        }
        
        for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }
        
        for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] = 'Q') {
                return false;
            }
        }
        
        return true;
    }
    
    function backtrack(row) {
        if (row === n) {
            result.push(board.map(r => r.join('')));
            return;
        }
        
        for (let col = 0; col < n; col++) {
            if (isValid(row, col)) {
                board[row][col] = 'Q';
                backtrack(row + 1);
                board[row][col] = '.';
            }
        }
    }
    
    backtrack(0);
    return result;
}

/**
 * Sudoku Solver
 * Resolve um Sudoku usando backtracking
 * @param {character[][]} board
 * @return {void}
 */
function solveSudoku(board) {
    function isValid(row, col, num) {
        for (let x = 0; x < 9; x++) {
            if (board[row][x] === num) {
                return false;
            }
        }
        
        for (let x = 0; x < 9; x++) {
            if (board[x][col] === num) {
                return false;
            }
        }
        
        const startRow = Math.floor(row / 3) * 3;
        const startCol = Math.floor(col / 3) * 3;
        
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (board[startRow + i][startCol + j] === num) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    function solve() {
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {
                if (board[row][col] === '.') {
                    for (let num = '1'; num <= '9'; num++) {
                        if (isValid(row, col, num)) {
                            board[row][col] = num;
                            
                            if (solve()) {
                                return true;
                            }
                            
                            board[row][col] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    solve();
}

console.log("N-Queens (n=4):");
const queensResult = solveNQueens(4);
queensResult.forEach((solution, idx) => {
    console.log(`Solução ${idx + 1}:`);
    solution.forEach(row => console.log(row));
    console.log();
});

console.log("\nSudoku Solver:");
const sudokuBoard = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
];
solveSudoku(sudokuBoard);
console.log("Sudoku resolvido:")
sudokuBoard.forEach(row => console.log(row.join(' ')));

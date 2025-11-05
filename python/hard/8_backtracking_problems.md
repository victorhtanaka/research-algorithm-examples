# Backtracking Problems (Hard)

## Descrição
Este arquivo contém três problemas clássicos que utilizam backtracking:

1. **solve_n_queens**: Resolve o problema das N rainhas, colocando N rainhas em um tabuleiro NxN de forma que nenhuma rainha ataque outra. Uma rainha pode atacar horizontal, vertical e diagonalmente.

2. **solve_sudoku**: Resolve um puzzle de Sudoku 9x9 preenchendo os espaços vazios (marcados com '.') de forma que cada linha, coluna e subgrade 3x3 contenha os dígitos de 1 a 9 sem repetição.

3. **permute**: Gera todas as permutações possíveis de uma lista de números usando backtracking.

Todos usam backtracking recursivo para explorar todas as possibilidades.

## Erros Presentes

1. **Erro de Sintaxe (Linha 38 - função is_valid do N-Queens)**: Atribuição ao invés de comparação
   - **Código incorreto**: `if board[i][j] = 'Q':`
   - **Código correto**: `if board[i][j] == 'Q':`
   - **Tipo**: Erro de sintaxe - Python não permite atribuição em condições if
   - **Consequência**: Causará SyntaxError ao executar

2. **Erro Conceitual (Linha 123 - função permute)**: Comentário sugere erro mas código está correto
   - **Código**: `result.append(current[:])`
   - **Observação**: `current[:]` é uma forma válida de copiar lista em Python, equivalente a `list(current)` ou `current.copy()`
   - **Tipo**: Comentário enganoso - não há erro real, apenas nota que existem formas alternativas
   - **Nota**: Este é um falso positivo intencional

3. **Erro de Sintaxe (Linha 159)**: Falta dois pontos após for
   - **Código incorreto**: `for row in sudoku_board`
   - **Código correto**: `for row in sudoku_board:`
   - **Tipo**: Erro de sintaxe obrigatório em Python
   - **Consequência**: Causará SyntaxError ao executar

# Backtracking Problems (Hard)

## Descrição
Este arquivo contém dois problemas clássicos que utilizam backtracking:

1. **N-Queens Problem**: Coloca N rainhas em um tabuleiro NxN de forma que nenhuma rainha ataque outra. Uma rainha pode atacar horizontal, vertical e diagonalmente.

2. **Sudoku Solver**: Resolve um puzzle de Sudoku 9x9 preenchendo os espaços vazios (marcados com '.') de forma que cada linha, coluna e subgrade 3x3 contenha os dígitos de 1 a 9 sem repetição.

Ambos usam backtracking recursivo para explorar todas as possibilidades.

## Erros Presentes

1. **Erro de Sintaxe (Linha 26 - função isValid do N-Queens)**: Atribuição ao invés de comparação
   - **Código incorreto**: `if (board[i][j] = 'Q')`
   - **Código correto**: `if (board[i][j] === 'Q')`
   - **Tipo**: Erro crítico - atribui valor ao invés de comparar, sempre avalia como truthy
   - **Consequência**: A validação da diagonal sempre retorna false incorretamente

2. **Erro Lógico/Sintaxe (Linha 97 - função solve do Sudoku)**: Comparação de string com número
   - **Código**: `for (let num = '1'; num <= '9'; num++)`
   - **Problema**: `num` é string mas o incremento `num++` converte para número
   - **Tipo**: Erro sutil - após primeira iteração, num vira número 2, mas comparação '2' <= '9' funciona por coerção
   - **Consequência**: Comportamento inesperado com tipos mistos

3. **Erro de Sintaxe (Linha 139)**: Falta ponto e vírgula
   - **Código incorreto**: `console.log("Sudoku resolvido:")`
   - **Código correto**: `console.log("Sudoku resolvido:");`
   - **Tipo**: Erro de sintaxe (tolerado pelo ASI)

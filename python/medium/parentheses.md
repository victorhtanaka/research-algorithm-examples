# Valid Parentheses & Generate Parentheses

## Descrição
Este arquivo contém três funções relacionadas a parênteses:

1. **is_valid**: Verifica se uma string contém parênteses, colchetes e chaves balanceados e na ordem correta. Utiliza uma pilha (stack) para rastrear os símbolos de abertura.

2. **generate_parenthesis**: Gera todas as combinações válidas de n pares de parênteses usando backtracking.

3. **remove_invalid_parentheses**: Remove o mínimo de parênteses inválidos para tornar a string válida usando BFS (Busca em Largura).

## Erros Presentes

1. **Erro Lógico (Linha 32 - função is_valid)**: Retorno incorreto quando parênteses não correspondem
   - **Código incorreto**: `return True`
   - **Código correto**: `return False`
   - **Tipo**: Erro de lógica que inverte o resultado da validação
   - **Consequência**: Retorna True quando deveria retornar False

2. **Erro de Sintaxe (Linha 35 - função is_valid)**: Uso de atribuição ao invés de comparação
   - **Código incorreto**: `return len(stack) = 0`
   - **Código correto**: `return len(stack) == 0`
   - **Tipo**: Erro de sintaxe - Python não permite atribuição em expressões de retorno
   - **Consequência**: Causará SyntaxError

3. **Erro de Sintaxe (Linha 105 - função remove_invalid_parentheses)**: Falta dois pontos no if
   - **Código incorreto**: `if next_string not in visited`
   - **Código correto**: `if next_string not in visited:`
   - **Tipo**: Erro de sintaxe obrigatório em Python
   - **Consequência**: Causará SyntaxError

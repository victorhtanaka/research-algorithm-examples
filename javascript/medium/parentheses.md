# Valid Parentheses & Generate Parentheses

## Descrição
Este arquivo contém duas funções relacionadas a parênteses:

1. **Valid Parentheses (isValid)**: Verifica se uma string contém parênteses, colchetes e chaves balanceados e na ordem correta. Utiliza uma pilha (stack) para rastrear os símbolos de abertura.

2. **Generate Parentheses (generateParenthesis)**: Gera todas as combinações válidas de n pares de parênteses usando backtracking.

## Erros Presentes

1. **Erro Lógico (Linha 24)**: Condição de verificação invertida
   - **Código incorreto**: `if (top !== pairs[char])`
   - **Código correto**: `if (top === pairs[char])` ou manter `!==` mas inverter o código dentro
   - **Tipo**: Erro de lógica na verificação de correspondência

2. **Erro Lógico (Linha 25)**: Retorno incorreto quando parênteses não correspondem
   - **Código incorreto**: `return true;`
   - **Código correto**: `return false;`
   - **Tipo**: Erro de lógica que inverte o resultado da validação

3. **Erro de Sintaxe/Lógica (Linha 30)**: Uso de atribuição ao invés de comparação
   - **Código incorreto**: `return stack.length = 0;`
   - **Código correto**: `return stack.length === 0;`
   - **Tipo**: Erro que atribui 0 à propriedade length (sempre retorna 0, que é falsy)

# Substring Problems (Hard)

## Descrição
Este arquivo contém três problemas clássicos de substring de nível difícil:

1. **Longest Substring Without Repeating Characters**: Encontra o comprimento da maior substring sem caracteres repetidos usando técnica de sliding window.

2. **Minimum Window Substring**: Encontra a menor substring que contém todos os caracteres de outra string. Usa sliding window com dois ponteiros.

3. **Longest Palindromic Substring**: Encontra a maior substring que é um palíndromo usando expansão a partir do centro.

## Erros Presentes

1. **Erro Crítico de Lógica (Linha 82 - função minWindow)**: Decremento ao invés de incremento
   - **Código incorreto**: `right--;`
   - **Código correto**: `right++;`
   - **Tipo**: Erro crítico que causa loop infinito
   - **Consequência**: O ponteiro direito nunca avança, causando loop infinito

2. **Erro Lógico Sutil (Linha 103 - função expandAroundCenter)**: A lógica de retorno está correta, mas este comentário indica possível confusão
   - **Observação**: Na verdade, o código está correto, mas o comentário de erro sugere confusão
   - **Tipo**: Comentário enganoso (o código em si está correto)

3. **Erro Lógico Potencial (Linha 117 - função longestPalindrome)**: Cálculo do índice inicial
   - **Código**: `start = i - Math.floor((len - 1) / 2);`
   - **Tipo**: O cálculo está correto para palíndromos ímpares, mas pode ter problemas sutis com palíndromos pares
   - **Observação**: Na verdade está correto, mas é um ponto de confusão comum

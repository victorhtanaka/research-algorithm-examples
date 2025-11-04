# Substring Problems (Hard)

## Descrição
Este arquivo contém quatro problemas clássicos de substring de nível difícil:

1. **length_of_longest_substring**: Encontra o comprimento da maior substring sem caracteres repetidos usando técnica de sliding window.

2. **min_window**: Encontra a menor substring que contém todos os caracteres de outra string. Usa sliding window com dois ponteiros.

3. **longest_palindrome**: Encontra a maior substring que é um palíndromo usando expansão a partir do centro.

4. **count_substrings**: Conta o número total de substrings palindrômicas.

## Erros Presentes

1. **Erro Crítico de Lógica (Linha 88 - função min_window)**: Decremento ao invés de incremento
   - **Código incorreto**: `right -= 1`
   - **Código correto**: `right += 1`
   - **Tipo**: Erro crítico que causa loop infinito
   - **Consequência**: O ponteiro direito nunca avança, causando loop infinito e o programa não termina

2. **Erro Lógico (Linha 146 - função count_substrings)**: Decremento ao invés de incremento
   - **Código incorreto**: `right -= 1`
   - **Código correto**: `right += 1`
   - **Tipo**: Erro de lógica que impede a expansão correta
   - **Consequência**: A função não expande corretamente para a direita, causando contagem incorreta de palíndromos

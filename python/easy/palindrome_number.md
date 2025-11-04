# Palindrome Number

## Descrição
Este algoritmo determina se um número inteiro é um palíndromo (lê-se igual de trás para frente). O arquivo contém duas implementações:

1. **is_palindrome**: Inverte o número digitalmente e compara com o número original
2. **is_palindrome_string**: Converte para string e usa dois ponteiros para verificar

Números negativos são automaticamente considerados não-palíndromos em ambas implementações.

## Erros Presentes

1. **Erro de Sintaxe (Linha 31 - função is_palindrome)**: Uso de atribuição ao invés de comparação
   - **Código incorreto**: `return original = reversed_num`
   - **Código correto**: `return original == reversed_num`
   - **Tipo**: Erro de sintaxe - Python não permite atribuição em expressões de retorno
   - **Consequência**: Causará SyntaxError ao executar

2. **Erro Lógico (Linha 43 - função is_palindrome_string)**: Índice direito incorreto
   - **Código incorreto**: `right = len(s)`
   - **Código correto**: `right = len(s) - 1`
   - **Tipo**: Erro de índice fora dos limites (IndexError)
   - **Consequência**: Causará IndexError ao tentar acessar `s[right]`

3. **Erro de Sintaxe (Linha 56)**: Falta dois pontos após if __name__ == "__main__"
   - **Código incorreto**: `if __name__ == "__main__"`
   - **Código correto**: `if __name__ == "__main__":`
   - **Tipo**: Erro de sintaxe obrigatório em Python
   - **Consequência**: Causará SyntaxError, o arquivo não executará

# Palindrome Number

## Descrição
Este algoritmo determina se um número inteiro é um palíndromo (lê-se igual de trás para frente). A solução inverte o número digitalmente e compara com o número original. Números negativos são automaticamente considerados não-palíndromos.

## Erros Presentes

1. **Erro de Sintaxe/Má Prática (Linha 13)**: Uso de `==` ao invés de `===`
   - **Código incorreto**: `if (x % 10 == 0 && x !== 0)`
   - **Código correto**: `if (x % 10 === 0 && x !== 0)`
   - **Tipo**: Má prática que pode causar comparações inesperadas com coerção de tipo

2. **Erro Lógico (Linha 26)**: Uso de atribuição ao invés de comparação
   - **Código incorreto**: `return original = reversed;`
   - **Código correto**: `return original === reversed;`
   - **Tipo**: Erro crítico - atribui valor ao invés de comparar, sempre retorna um valor truthy

3. **Erro de Sintaxe (Linha 33)**: Falta ponto e vírgula no final da linha
   - **Código incorreto**: `console.log(isPalindrome(0))`
   - **Código correto**: `console.log(isPalindrome(0));`
   - **Tipo**: Erro de sintaxe (embora JavaScript tenha ASI - Automatic Semicolon Insertion)

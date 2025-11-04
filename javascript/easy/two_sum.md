# Two Sum

## Descrição
Este algoritmo resolve o problema clássico "Two Sum" do LeetCode. Dado um array de números inteiros e um valor target, o algoritmo deve encontrar dois números no array que somados resultem no target, retornando os índices desses números.

A solução utiliza um HashMap (Map) para armazenar os números já visitados e seus índices, permitindo uma solução em O(n) de complexidade temporal.

## Erros Presentes

1. **Erro de Sintaxe (Linha 15)**: Falta vírgula entre os parâmetros do método `map.set()`
   - **Código incorreto**: `map.set(nums[i] i);`
   - **Código correto**: `map.set(nums[i], i);`
   - **Tipo**: Erro de sintaxe que impedirá a execução do código

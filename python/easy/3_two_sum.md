# Two Sum

## Descrição
Este algoritmo resolve o problema clássico "Two Sum" do LeetCode. Dado um array de números inteiros e um valor target, o algoritmo deve encontrar dois números no array que somados resultem no target, retornando os índices desses números.

A solução utiliza um dicionário (HashMap) para armazenar os números já visitados e seus índices, permitindo uma solução em O(n) de complexidade temporal e O(n) de complexidade espacial.

## Erros Presentes

1. **Erro Conceitual/Comentário Enganoso (Linha 23)**: O comentário sugere erro, mas o código está correto
   - **Código**: `num_map[nums[i]] = i`
   - **Comentário incorreto**: "falta incrementar antes de usar"
   - **Tipo**: O código está correto - não há erro real aqui, apenas um comentário enganoso
   - **Observação**: Este é um falso positivo intencional para testar a capacidade da IA de identificar quando um comentário sugere erro mas o código está correto

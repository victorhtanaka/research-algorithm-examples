# Binary Search & Search Insert Position

## Descrição
Este arquivo contém duas implementações relacionadas à busca binária:

1. **Binary Search**: Implementa busca binária clássica em um array ordenado, retornando o índice do elemento procurado ou -1 se não encontrado.

2. **Search Insert Position**: Encontra a posição onde um elemento deveria ser inserido em um array ordenado para manter a ordem.

Ambos os algoritmos utilizam a técnica de dividir e conquistar com complexidade O(log n).

## Erros Presentes

1. **Erro Lógico (Linha 17 - função binarySearch)**: Atualização incorreta do ponteiro esquerdo
   - **Código incorreto**: `left = mid;`
   - **Código correto**: `left = mid + 1;`
   - **Tipo**: Erro de lógica que causará loop infinito quando o elemento procurado está à direita
   - **Consequência**: O algoritmo pode entrar em loop infinito ou não encontrar o elemento

2. **Erro de Sintaxe (Linha 56)**: Falta ponto e vírgula
   - **Código incorreto**: `console.log(searchInsert([1, 3, 5, 6], 7))`
   - **Código correto**: `console.log(searchInsert([1, 3, 5, 6], 7));`
   - **Tipo**: Erro de sintaxe (embora tolerado pelo ASI do JavaScript)

# Binary Search & Search Insert Position

## Descrição
Este arquivo contém três implementações relacionadas à busca binária:

1. **binary_search**: Implementa busca binária clássica iterativa em um array ordenado, retornando o índice do elemento procurado ou -1 se não encontrado.

2. **search_insert**: Encontra a posição onde um elemento deveria ser inserido em um array ordenado para manter a ordem.

3. **binary_search_recursive**: Versão recursiva da busca binária.

Todos os algoritmos utilizam a técnica de dividir e conquistar com complexidade O(log n).

## Erros Presentes

1. **Erro Lógico (Linha 26 - função binary_search)**: Atualização incorreta do ponteiro esquerdo
   - **Código incorreto**: `left = mid`
   - **Código correto**: `left = mid + 1`
   - **Tipo**: Erro de lógica que causará loop infinito quando o elemento procurado está à direita
   - **Consequência**: O algoritmo pode entrar em loop infinito ou não encontrar o elemento

2. **Erro de Tipo (Linha 74 - função binary_search_recursive)**: Divisão float ao invés de inteira
   - **Código incorreto**: `mid = (left + right) / 2`
   - **Código correto**: `mid = (left + right) // 2`
   - **Tipo**: Erro de tipo - índice de lista deve ser inteiro, não float
   - **Consequência**: Causará TypeError ao tentar usar float como índice de lista

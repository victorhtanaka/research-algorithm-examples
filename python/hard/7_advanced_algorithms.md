# Advanced Algorithms (Hard)

## Descrição
Este arquivo contém quatro algoritmos avançados de nível difícil:

1. **find_median_sorted_arrays**: Encontra a mediana de dois arrays ordenados em tempo O(log(min(m,n))) usando busca binária nas partições.

2. **is_match**: Implementa matching de expressões regulares suportando '.' (qualquer caractere) e '*' (zero ou mais do caractere anterior) usando programação dinâmica com memoização.

3. **trap**: Calcula quanta água pode ser aprisionada entre barras de diferentes alturas usando técnica de dois ponteiros.

4. **max_sliding_window**: Encontra o máximo em cada janela deslizante de tamanho k usando deque (double-ended queue).

## Erros Presentes

1. **Erro de Sintaxe/Lógica (Linha 81 - função is_match)**: Uso de operador bitwise ao invés de lógico
   - **Código incorreto**: `memo[(i, j)] = first_match & dp(i + 1, j + 1)`
   - **Código correto**: `memo[(i, j)] = first_match and dp(i + 1, j + 1)`
   - **Tipo**: Erro sutil - operador bitwise `&` ao invés de lógico `and`
   - **Consequência**: Pode causar resultados incorretos em algumas situações devido ao comportamento diferente dos operadores
   - **Nota**: Em Python, `&` é operador bitwise e `and` é operador lógico; ambos funcionam com booleanos mas têm precedência e comportamento diferentes

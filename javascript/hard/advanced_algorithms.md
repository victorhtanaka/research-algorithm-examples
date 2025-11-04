# Advanced Algorithms (Hard)

## Descrição
Este arquivo contém três algoritmos avançados de nível difícil:

1. **Median of Two Sorted Arrays**: Encontra a mediana de dois arrays ordenados em tempo O(log(min(m,n))) usando busca binária nas partições.

2. **Regular Expression Matching**: Implementa matching de expressões regulares suportando '.' (qualquer caractere) e '*' (zero ou mais do caractere anterior) usando programação dinâmica com memoização.

3. **Trapping Rain Water**: Calcula quanta água pode ser aprisionada entre barras de diferentes alturas usando técnica de dois ponteiros.

## Erros Presentes

1. **Erro Conceitual (Linha 39)**: Código está correto, mas comentário sugere erro
   - **Observação**: O código `low = partition1 + 1;` está correto
   - **Tipo**: Comentário enganoso (não há erro real aqui)

2. **Erro de Boas Práticas (Linha 44)**: Mensagem de erro em português
   - **Código**: `throw new Error("Arrays não estão ordenados");`
   - **Melhor prática**: Mensagens de erro deveriam estar em inglês em código
   - **Tipo**: Má prática, não erro funcional

3. **Erro de Sintaxe (Linha 79 - função isMatch)**: Uso de operador bitwise ao invés de lógico
   - **Código incorreto**: `memo[key] = firstMatch & dp(i + 1, j + 1);`
   - **Código correto**: `memo[key] = firstMatch && dp(i + 1, j + 1);`
   - **Tipo**: Erro sutil - operador bitwise `&` ao invés de lógico `&&`
   - **Consequência**: Pode causar resultados incorretos em algumas situações

4. **Erro de Sintaxe (Linha 111 - função trap)**: Falta ponto e vírgula
   - **Código incorreto**: `water += rightMax - height[right]`
   - **Código correto**: `water += rightMax - height[right];`
   - **Tipo**: Erro de sintaxe (tolerado pelo ASI)

5. **Erro Lógico Potencial (Linha 39)**: O comentário indica erro mas o código está correto
   - **Tipo**: Falso positivo no comentário de erro

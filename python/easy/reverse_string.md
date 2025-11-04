# Reverse String

## Descrição
Este algoritmo inverte uma string representada como uma lista de caracteres, fazendo a modificação in-place (sem usar espaço extra significativo). A técnica utilizada é a abordagem de dois ponteiros, onde um ponteiro começa no início e outro no final da lista, e eles se movem em direção ao centro trocando os elementos.

O arquivo também contém uma segunda implementação que demonstra um erro comum ao tentar reverter usando slicing do Python.

## Erros Presentes

1. **Erro Lógico (Linha 20 - função reverse_string)**: Incremento incorreto do ponteiro direito
   - **Código incorreto**: `right += 1`
   - **Código correto**: `right -= 1`
   - **Tipo**: Erro de lógica que causará um loop infinito
   - **Consequência**: O programa entrará em loop infinito pois ambos os ponteiros se movem na mesma direção

2. **Erro Conceitual (Linha 27 - função reverse_string_v2)**: Modificação não in-place
   - **Código incorreto**: `s = s[::-1]`
   - **Código correto**: `s[:] = s[::-1]` (para modificar in-place)
   - **Tipo**: Erro conceitual - cria uma nova lista local ao invés de modificar a lista original
   - **Consequência**: A função não tem efeito na lista original passada como parâmetro
